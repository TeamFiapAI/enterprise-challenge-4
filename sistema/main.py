from fastapi import FastAPI
import uvicorn
from routers import sensor_router
from routers.maintenance_router import router as maintenance_router

app = FastAPI(
    title="Enterprise Challenge - Sprint 4",
    description="Na Indústria 4.0, sensores conectados geram dados que precisam" \
    " fluir de forma confiável até camadas analíticas e de decisão (ML, dashboards, alertas)." \
    " Esse é exatamente o cenário que vocês já planejaram (arquitetura e pipeline)," \
    " simularam (ESP32 + sensores) e modelaram (banco relacional + ML). Agora," \
    " vamos “costurar” tudo em um MVP integrado, com ênfase em observabilidade e reprodutibilidade.",
    version="1.0.0"
)

# Rota com prefixo /dados
app.include_router(sensor_router.router, prefix="/dados", tags=["Sensores"])
app.include_router(maintenance_router, prefix="/manutencao", tags=["Manutenção"])

# Entry point
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)