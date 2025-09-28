# Hermes Reply – Entrega 4 (MVP Integrado)

MVP ponta-a-ponta **simulador → ingestão (FastAPI) → SQLite → ML (scikit-learn) → Dashboard (Streamlit + alertas)**.

## ⚙️ Como rodar (3 passos)

1) Criar venv e instalar dependências
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

2) Criar banco e carregar massa inicial
```bash
python db/init_db.py
python db/load_sample_data.py
```

3) Em 2 terminais separados
```bash
uvicorn ingest.api.main:app --reload --port 8000
streamlit run dashboard/app.py
```

(Se quiser leituras ao vivo)
```bash
python ingest/simulator/send_sensor_data.py
```

Para treinar modelo:
```bash
python ml/train.py
python ml/infer.py
```
