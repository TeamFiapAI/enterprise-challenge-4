import streamlit as st
import sqlite3, os, pandas as pd, matplotlib.pyplot as plt

DB = os.path.join(os.path.dirname(__file__), "../data.db")
ALERT_LOG = os.path.join(os.path.dirname(__file__), "alerts.log")

st.set_page_config(page_title="Industrial MVP", layout="wide")
st.title("🏭 Hermes Reply – MVP Industrial (PR1→PR5)")

@st.cache_data(ttl=5)
def load_data():
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query("SELECT ts, device_id, temperature, humidity, vibration FROM sensor_reading ORDER BY ts", conn)
    conn.close()
    if len(df)==0: return df
    df["ts"] = pd.to_datetime(df["ts"])
    return df

df = load_data()
if len(df)==0:
    st.warning("Sem dados. Rode a API /ingest + simulador ou carregue o CSV (db/load_sample_data.py).")
    st.stop()

c1,c2,c3 = st.columns(3)
last = df.iloc[-1]
c1.metric("🌡️ Temp (última)", f"{last.temperature:.2f} °C")
c2.metric("💧 Umidade (última)", f"{last.humidity:.2f} %")
c3.metric("🪫 Vibração (última)", f"{last.vibration:.4f} g")
st.metric("📦 Leituras totais", len(df))

st.subheader("Séries")
col1,col2 = st.columns(2)
with col1:
    fig,ax = plt.subplots(); ax.plot(df["ts"], df["temperature"]); ax.set_title("Temperatura"); st.pyplot(fig)
with col2:
    fig,ax = plt.subplots(); ax.plot(df["ts"], df["vibration"]); ax.set_title("Vibração"); st.pyplot(fig)

st.subheader("⚠️ Alertas")
th = st.slider("Threshold de temperatura (°C)", 20.0, 50.0, 30.0, 0.5)
if last.temperature > th:
    st.error(f"ALERTA: {last.temperature:.2f}°C > {th:.2f}°C")
    with open(ALERT_LOG,"a") as f:
        f.write(f"[alert] ts={last.ts} temp={last.temperature:.2f} th={th:.2f}\n")
else:
    st.success(f"OK: {last.temperature:.2f}°C ≤ {th:.2f}°C")

if os.path.exists(ALERT_LOG):
    with open(ALERT_LOG,"rb") as fh:
        st.download_button("Baixar log de alertas", data=fh.read(), file_name="alerts.log")
