PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS device (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  device_id TEXT UNIQUE NOT NULL,
  location TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS sensor_reading (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  device_id TEXT NOT NULL,
  ts TEXT NOT NULL,
  temperature REAL,
  humidity REAL,
  vibration REAL,
  FOREIGN KEY (device_id) REFERENCES device(device_id)
);

CREATE INDEX IF NOT EXISTS idx_sensor_device_ts ON sensor_reading(device_id, ts);
