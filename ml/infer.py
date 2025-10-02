import sqlite3, os, pandas as pd, numpy as np, joblib
DB = os.path.join(os.path.dirname(__file__), "../data.db")
MODEL = os.path.join(os.path.dirname(__file__), "model.pkl")
ALERTS = os.path.join(os.path.dirname(__file__), "../dashboard/alerts.log")

def latest_window(df, window=3):
    feats=[]
    for w in range(window):
        j = len(df)-1 - w
        feats += [df.loc[j,"temperature"], df.loc[j,"humidity"], df.loc[j,"vibration"]]
    return np.array(feats).reshape(1,-1)

model = joblib.load(MODEL)
conn = sqlite3.connect(DB)
df = pd.read_sql_query("SELECT * FROM sensor_reading ORDER BY ts", conn)
conn.close()
df["ts"] = pd.to_datetime(df["ts"])
X = latest_window(df, window=3)
y_hat = float(model.predict(X)[0])
last_temp = float(df.iloc[-1]["temperature"])
THRESH = 30.0
triggered = y_hat > THRESH
os.makedirs(os.path.dirname(ALERTS), exist_ok=True)
with open(ALERTS,"a") as f:
    f.write(f"[infer] pred={y_hat:.2f} last={last_temp:.2f} TH={THRESH} ALERT={triggered}\n")
print({"pred": y_hat, "last": last_temp, "threshold": THRESH, "alert": bool(triggered)})
