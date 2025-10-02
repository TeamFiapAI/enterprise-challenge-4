import sqlite3, os
DB = os.path.join(os.path.dirname(__file__), "../data.db")
SQL = os.path.join(os.path.dirname(__file__), "create_tables.sql")
conn = sqlite3.connect(DB)
with open(SQL) as f: conn.executescript(f.read())
conn.commit(); conn.close(); print("Banco criado:", DB)
