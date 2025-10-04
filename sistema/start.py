import os
import subprocess
import webbrowser

env = os.environ.copy()
env["PYTHONPATH"] = os.getcwd()

FASTAPI_PORT = 8000
STREAMLIT_PORT = 8501

# FastAPI
print("Iniciando FastAPI...")
fastapi_proc = subprocess.Popen(
    ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", f"--port={FASTAPI_PORT}"],
    env=env
)

# Abre /docs no navegador
webbrowser.open(f"http://localhost:{FASTAPI_PORT}/docs")

# Streamlit
print("Iniciando Streamlit...")
streamlit_proc = subprocess.Popen(
    [
        "streamlit", "run", "dashboard/home.py",
        f"--server.port={STREAMLIT_PORT}",
        "--server.headless", "true"
    ],
    env=env
)

# Abre apenas a URL local
webbrowser.open(f"http://localhost:{STREAMLIT_PORT}")

try:
    fastapi_proc.wait()
    streamlit_proc.wait()
except KeyboardInterrupt:
    print("Encerrando serviços...")
    fastapi_proc.terminate()
    streamlit_proc.terminate()