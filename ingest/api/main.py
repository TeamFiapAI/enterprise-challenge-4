from fastapi import FastAPI, Request
import sqlite3, os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "../../data.db")
app = FastAPI(title="Ingestion API")

def conn():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ingest")
async def ingest(req: Request):
    p = await req.json()
    device_id   = p.get("device_id", "esp32-A1")
    ts          = p.get("timestamp") or datetime.utcnow().isoformat()
    temperature = p.get("temperature")
    humidity    = p.get("humidity")
    vibration   = p.get("vibration")
    with conn() as c:
        cur=c.cursor()
        cur.execute("INSERT OR IGNORE INTO device(device_id) VALUES(?)",(device_id,))
        cur.execute("INSERT INTO sensor_reading(device_id, ts, temperature, humidity, vibration) VALUES (?,?,?,?,?)",
                    (device_id, ts, temperature, humidity, vibration))
        c.commit()
    return {"status":"ok"}
