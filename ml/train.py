import sqlite3, os, pandas as pd, numpy as np, joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

DB = os.path.join(os.path.dirname(__file__), "../data.db")
MODEL = os.path.join(os.path.dirname(__file__), "model.pkl")
PLOT = os.path.join(os.path.dirname(__file__), "../prints/ml_metrics.png")

def load_df():
    conn = sqlite3.connect(DB)
    df = pd.read_sql_query("SELECT ts, temperature, humidity, vibration FROM sensor_reading WHERE temperature IS NOT NULL ORDER BY ts", conn)
    conn.close()
    df["ts"] = pd.to_datetime(df["ts"])
    return df.sort_values("ts").reset_index(drop=True)

def make_supervised(df, window=3):
    X, y = [], []
    for i in range(window, len(df)-1):
        feats=[]
        for w in range(window):
            j = i - w
            feats += [df.loc[j,"temperature"], df.loc[j,"humidity"], df.loc[j,"vibration"]]
        X.append(feats); y.append(df.loc[i+1,"temperature"])
    return np.array(X), np.array(y)

df = load_df()
if len(df) < 50:
    print("Poucos dados. Gere mais leituras ou carregue o CSV."); raise SystemExit(0)
X,y = make_supervised(df, window=3)
Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=0.2,shuffle=False)
model = LinearRegression().fit(Xtr,ytr)
pred = model.predict(Xte)
mae = mean_absolute_error(yte,pred)
print(f"MAE: {mae:.3f}")
joblib.dump(model, MODEL)

fig = plt.figure()
plt.plot(range(len(yte)), yte, label="real")
plt.plot(range(len(pred)), pred, label="previsto")
plt.legend(); plt.title(f"Temperatura - MAE {mae:.3f}")
os.makedirs(os.path.dirname(PLOT), exist_ok=True)
fig.savefig(PLOT)
print("Gráfico salvo em", PLOT)
