import os
import pandas as pd
import numpy as np
from datetime import timedelta
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from joblib import dump, load
from repository.oracle import carregar_registros_df as repo_carregar_registros_df

modelo = None
scaler = None
colunas_modelo = None
df_limpo = None
window = "15min"
contamination = 0.02
model_path = os.getenv("MODEL_PATH", "models/iforest_registros.joblib")

def carregar_registros_df():
    return repo_carregar_registros_df()

def _prepare_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza nomes e tipos esperados pelo pipeline.
    """
    df = df.copy()
    rename_map = {}
    for c in df.columns:
        lc = c.lower()
        if lc == "data_coleta":   rename_map[c] = "ts"
        if lc == "id_maquina":    rename_map[c] = "id_maquina"
        if lc == "id_operador":   rename_map[c] = "id_operador"
        if lc == "gasao":         rename_map[c] = "GASAO"
        if lc == "gasdo":         rename_map[c] = "GASDO"
        if lc == "temperatura":   rename_map[c] = "TEMPERATURA"
        if lc == "umidade":       rename_map[c] = "UMIDADE"
        if lc == "potenciometro": rename_map[c] = "POTENCIOMETRO"
        if lc == "alarme":        rename_map[c] = "ALARME"
    df.rename(columns=rename_map, inplace=True)

    if "ts" not in df.columns:
        raise ValueError("Coluna 'data_coleta' ausente (esperada como 'ts' após rename).")
    if not np.issubdtype(df["ts"].dtype, np.datetime64):
        df["ts"] = pd.to_datetime(df["ts"])

    df = df.sort_values(["id_maquina","ts"]).reset_index(drop=True)

    for col in ["TEMPERATURA","UMIDADE","POTENCIOMETRO","GASAO","GASDO","ALARME"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    keep_cols = ["ts","id_maquina","id_operador","TEMPERATURA","UMIDADE","POTENCIOMETRO","GASAO","GASDO","ALARME"]
    df = df[[c for c in keep_cols if c in df.columns]].dropna(subset=["ts","id_maquina","TEMPERATURA","UMIDADE","POTENCIOMETRO","GASAO","GASDO"])
    return df

def _make_features(df: pd.DataFrame, win: str) -> pd.DataFrame:
    """
    Agrega por janela (ex.: 15min) e retorna uma linha por (maquina, janela).
    """
    if df.empty:
        return pd.DataFrame()

    feats = []
    for mid, g in df.groupby("id_maquina"):
        g = g.set_index("ts")
        agg = g.resample(win).agg({
            "TEMPERATURA": ["mean","std","max","min"],
            "UMIDADE": ["mean","std","max","min"],
            "POTENCIOMETRO": ["mean","std","max","min"],
            "GASAO": ["mean","std","max","min"],
            "GASDO": ["mean","std","max","min"],
            "ALARME": "mean"
        }).dropna()
        if not agg.empty:
            agg.columns = ['_'.join([c for c in col if c]) for col in agg.columns]
            agg["id_maquina"] = mid
            feats.append(agg.reset_index())
    if not feats:
        return pd.DataFrame()
    X = pd.concat(feats, ignore_index=True)
    return X

def treinar_modelo_kpis():
    """
    Treina IsolationForest em features de janelas a partir de toda a REGISTROS.
    """
    global modelo, scaler, colunas_modelo, df_limpo

    df_raw = carregar_registros_df()
    df = _prepare_df(df_raw)
    df_limpo = df.copy()

    X = _make_features(df, window)
    if X.empty:
        raise RuntimeError("Sem dados suficientes para treinar (features vazias).")

    colunas_modelo = [c for c in X.columns if c not in ("ts","id_maquina")]

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("iso", IsolationForest(
            n_estimators=300,
            contamination=contamination,
            random_state=42,
            n_jobs=-1
        ))
    ])
    pipe.fit(X[colunas_modelo])

    os.makedirs(os.path.dirname(model_path) or ".", exist_ok=True)
    dump({"pipe": pipe, "features": colunas_modelo, "window": window}, model_path)

    modelo = pipe
    scaler = pipe.named_steps["scaler"]

    print("✅ Modelo KPIs/Anomalias treinado com sucesso!")
    return {"windows_treinadas": len(X), "features": colunas_modelo}

def _ensure_model():
    global modelo, scaler, colunas_modelo, window
    if modelo is not None and colunas_modelo is not None:
        return
    if not os.path.exists(model_path):
        treinar_modelo_kpis()
        return
    obj = load(model_path)
    modelo = obj["pipe"]
    colunas_modelo = obj["features"]
    window = obj.get("window", window)
    scaler = modelo.named_steps.get("scaler")

def _one_row_features_from_latest(df_maquina: pd.DataFrame) -> pd.DataFrame:
    """
    Recria a **última** janela de features para a máquina.
    Busca ~1h anterior e resample para 'window', retornando a última linha.
    """
    if df_maquina.empty:
        return pd.DataFrame()

    end_ts = df_maquina["ts"].max()
    df_slice = df_maquina[(df_maquina["ts"] > end_ts - pd.Timedelta("1h")) & (df_maquina["ts"] <= end_ts)]
    Xs = _make_features(df_slice, window)
    if Xs.empty:
        return pd.DataFrame()
    return Xs.sort_values("ts").tail(1)

def _kpis_from_df(df_maquina_24h: pd.DataFrame) -> dict:
    if df_maquina_24h.empty:
        return {"count": 0}
    def block(s, prefix):
        return {
            f"{prefix}_mean": float(s.mean()),
            f"{prefix}_std": float(s.std(ddof=0)) if len(s) > 1 else 0.0,
            f"{prefix}_p95": float(s.quantile(0.95)) if len(s) > 1 else float(s.iloc[0]),
            f"{prefix}_max": float(s.max())
        }
    k = {"count": int(len(df_maquina_24h))}
    k.update(block(df_maquina_24h["TEMPERATURA"], "temp"))
    k.update(block(df_maquina_24h["UMIDADE"], "umid"))
    k.update(block(df_maquina_24h["POTENCIOMETRO"], "pot"))
    k.update(block(df_maquina_24h["GASAO"], "gasao"))
    k.update(block(df_maquina_24h["GASDO"], "gasdo"))
    if "ALARME" in df_maquina_24h:
        k["alarme_rate"] = float(df_maquina_24h["ALARME"].mean())
    else:
        k["alarme_rate"] = 0.0
    return k

def prever_kpis(dados: dict) -> dict:
    """
    Entrada (um novo pulso, no mesmo espírito do seu prever_vazao):
      dados = {
        "id_maquina": int, "id_operador": int, "data_coleta": "ISO",
        "temperatura": float, "umidade": float, "potenciometro": float,
        "gasAO": float, "gasDO": float, "alarme": int
      }

    Comportamento:
      - Garante que há modelo em disco (ou treina).
      - Lê a base completa (sem filtro), anexa o novo ponto **em memória**
        (o treino do modelo continua batch, mas a pontuação usa a última janela).
      - Calcula **KPIs de 24h** para a máquina.
      - Cria features da última janela e retorna **score/anomalia**.
    """
    _ensure_model()

    df_hist = _prepare_df(carregar_registros_df())

    novo = pd.DataFrame([{
        "ts": pd.to_datetime(dados["data_coleta"]),
        "id_maquina": int(dados["id_maquina"]),
        "id_operador": int(dados["id_operador"]),
        "TEMPERATURA": float(dados["temperatura"]),
        "UMIDADE": float(dados["umidade"]),
        "POTENCIOMETRO": float(dados["potenciometro"]),
        "GASAO": float(dados["gasAO"]),
        "GASDO": float(dados["gasDO"]),
        "ALARME": int(dados.get("alarme", 0))
    }])
    df_all = pd.concat([df_hist, novo], ignore_index=True).sort_values(["id_maquina","ts"])

    idm = int(dados["id_maquina"])
    end_ts = novo["ts"].iloc[0]
    df_24h = df_all[(df_all["id_maquina"] == idm) &
                    (df_all["ts"] >= end_ts - pd.Timedelta("24h")) &
                    (df_all["ts"] <= end_ts)]
    kpis = _kpis_from_df(df_24h)

    X_last = _one_row_features_from_latest(df_all[df_all["id_maquina"] == idm])
    if X_last.empty:
        return {"kpis": kpis, "anomalia": 0, "score": float("nan"), "id_maquina": idm}

    scores = modelo.decision_function(X_last[colunas_modelo])
    preds = modelo.predict(X_last[colunas_modelo])
    score = float(scores[0])
    anom = int(preds[0] == -1)

    return {
        "id_maquina": idm,
        "window_ts": X_last["ts"].iloc[0].isoformat(),
        "score": score,
        "anomalia": anom,
        "kpis": kpis
    }

def get_modelo():
    _ensure_model()
    return modelo

def get_df_limpo():
    return df_limpo
