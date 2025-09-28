import sqlite3, csv, os
DB = os.path.join(os.path.dirname(__file__), '../data.db')
CSV = os.path.join(os.path.dirname(__file__), 'sample.csv')
conn = sqlite3.connect(DB); cur=conn.cursor()
cur.execute("INSERT OR IGNORE INTO device(device_id, location) VALUES(?,?)", ("esp32-A1","linha-01"))
with open(CSV) as f:
    r=csv.DictReader(f); rows=0
    for x in r:
        cur.execute("INSERT INTO sensor_reading(device_id, ts, temperature, humidity, vibration) VALUES (?,?,?,?,?)",
                    ("esp32-A1", x["timestamp"], float(x["temperature"]), float(x["humidity"]), float(x["vibration"])))
        rows+=1
conn.commit(); conn.close(); print("Linhas carregadas:", rows)
