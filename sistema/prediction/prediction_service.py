import pandas as pd
from datetime import timedelta
from sqlalchemy import text

import prediction.model as ml
from prediction.model import _prepare_df
from repository.oracle import get_conn, inserir_registros_esp32, carregar_registros_df

def _kpis_from_df(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"count": 0, "alarme_rate": 0.0}
    def block(s, prefix):
        return {
            f"{prefix}_mean": float(s.mean()),
            f"{prefix}_std": float(s.std(ddof=0)) if len(s) > 1 else 0.0,
            f"{prefix}_p95": float(s.quantile(0.95)) if len(s) > 1 else float(s.iloc[0]),
            f"{prefix}_max": float(s.max())
        }
    k = {"count": int(len(df))}
    for name in ["TEMPERATURA","UMIDADE","POTENCIOMETRO","GASAO","GASDO"]:
        if name in df:
            k.update(block(df[name], name.lower()))
    k["alarme_rate"] = float(df["ALARME"].mean()) if "ALARME" in df else 0.0
    return k

def _one_row_features_from_latest(df_maquina: pd.DataFrame, win: str) -> pd.DataFrame:
    if df_maquina.empty:
        return pd.DataFrame()
    end_ts = df_maquina["ts"].max()
    df_slice = df_maquina[(df_maquina["ts"] > end_ts - pd.Timedelta("1h")) & (df_maquina["ts"] <= end_ts)]
    if df_slice.empty:
        return pd.DataFrame()

    g = df_slice.set_index("ts").sort_index()
    grp = g.resample(win)
    out = pd.DataFrame(index=grp.mean().index)
    for c in ["TEMPERATURA","UMIDADE","POTENCIOMETRO","GASAO","GASDO"]:
        out[f"{c}_mean"] = grp[c].mean()
        out[f"{c}_max"]  = grp[c].max()
        out[f"{c}_min"]  = grp[c].min()
        out[f"{c}_std"]  = grp[c].std(ddof=0).fillna(0.0)
    out["ALARME_mean"] = grp["ALARME"].mean() if "ALARME" in g else 0.0
    out = out.dropna(how="all")
    if out.empty:
        return pd.DataFrame()
    out = out.reset_index().rename(columns={"index":"ts"})
    return out.tail(1)

def _carregar_maquina_periodo(id_maquina: int, start_ts: pd.Timestamp, end_ts: pd.Timestamp) -> pd.DataFrame:
    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT 
                  id_registro, id_maquina, id_operador, data_coleta,
                  temperatura, umidade, potenciometro, gasAO, gasDO, alarme
                FROM registros
                WHERE id_maquina = :m
                  AND data_coleta >= :ini
                  AND data_coleta <= :fim
                ORDER BY data_coleta
            """, m=id_maquina, ini=start_ts, fim=end_ts)
            rows = cursor.fetchall()
            cols = [c[0].lower() for c in cursor.description]
            df = pd.DataFrame(rows, columns=cols)
        return _prepare_df(df)
    finally:
        if conn:
            conn.close()

def _carregar_maquina_24h(id_maquina: int, end_ts: pd.Timestamp) -> pd.DataFrame:
    start_ts = end_ts - pd.Timedelta("24h")
    return _carregar_maquina_periodo(id_maquina, start_ts, end_ts)

def pontuar_pulso(pulso: dict) -> dict:

    inserir_registros_esp32([pulso])

    end_ts = pd.to_datetime(pulso["data_coleta"])
    idm = int(pulso["id_maquina"])

    df_recent = _carregar_maquina_periodo(idm, end_ts - pd.Timedelta("1h"), end_ts)

    df_new = pd.DataFrame([{
        "ts": end_ts,
        "id_maquina": idm,
        "id_operador": int(pulso["id_operador"]),
        "TEMPERATURA": float(pulso["temperatura"]),
        "UMIDADE": float(pulso["umidade"]),
        "POTENCIOMETRO": float(pulso["potenciometro"]),
        "GASAO": float(pulso["gasAO"]),
        "GASDO": float(pulso["gasDO"]),
        "ALARME": int(pulso.get("alarme", 0))
    }])
    df_recent = pd.concat([df_recent, df_new], ignore_index=True).sort_values("ts")

    df_24h = _carregar_maquina_24h(idm, end_ts)
    if df_24h.empty:
        df_24h = df_recent.copy()

    kpis = _kpis_from_df(df_24h)

    X_last = _one_row_features_from_latest(df_recent, ml.window)
    if X_last.empty:
        return {
            "id_maquina": idm,
            "window_ts": None,
            "score": float("nan"),
            "anomalia": 0,
            "kpis_24h": kpis
        }

    modelo = ml.get_modelo()
    scores = modelo.decision_function(X_last[ml.colunas_modelo])
    preds  = modelo.predict(X_last[ml.colunas_modelo])
    score = float(scores[0])
    anom = int(preds[0] == -1)

    return {
        "id_maquina": idm,
        "window_ts": X_last["ts"].iloc[0].isoformat(),
        "score": score,
        "anomalia": anom,
        "kpis_24h": kpis
    }

def kpis_overview() -> dict:
    df_raw = carregar_registros_df()
    df = _prepare_df(df_raw)
    if df.empty:
        return {"last_ts": None, "overall": {"count": 0, "alarme_rate": 0.0}, "maquinas": {}}

    overall = _kpis_from_df(df)
    maquinas = {int(mid): _kpis_from_df(g) for mid, g in df.groupby("id_maquina")}
    last_ts = df["ts"].max().isoformat()
    return {"last_ts": last_ts, "overall": overall, "maquinas": maquinas}

def kpis_da_maquina(id_maquina: int) -> dict:
    df_raw = carregar_registros_df()
    df = _prepare_df(df_raw)
    g = df[df["id_maquina"] == id_maquina]
    if g.empty:
        return {"id_maquina": id_maquina, "count": 0, "alarme_rate": 0.0}
    out = _kpis_from_df(g)
    out["id_maquina"] = id_maquina
    out["last_ts"] = g["ts"].max().isoformat()
    return out

def kpis_do_operador(id_operador: int) -> dict:
    df_raw = carregar_registros_df()
    df = _prepare_df(df_raw)
    g = df[df["id_operador"] == id_operador]
    if g.empty:
        return {"id_operador": id_operador, "count": 0, "alarme_rate": 0.0}
    out = _kpis_from_df(g)
    out["id_operador"] = id_operador
    out["last_ts"] = g["ts"].max().isoformat()
    return out

