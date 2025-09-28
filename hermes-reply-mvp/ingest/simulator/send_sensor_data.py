import requests, random, time, datetime
API = "http://127.0.0.1:8000/ingest"
def jitter(v,s): return round(v + random.uniform(-s,s), 3)
while True:
    data = {
        "device_id":"esp32-A1",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "temperature": jitter(27.5,1.8),
        "humidity": jitter(58.0,4.0),
        "vibration": abs(jitter(0.010,0.008))
    }
    r=requests.post(API,json=data,timeout=5)
    print(r.status_code, data)
    time.sleep(2)
