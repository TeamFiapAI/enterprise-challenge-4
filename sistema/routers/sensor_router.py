from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.logical_table import completar_registros_esp32
from repository.oracle import inserir_registros_esp32
from prediction.prediction_service import pontuar_pulso
from prediction.prediction_service import kpis_overview, kpis_da_maquina, kpis_do_operador


router = APIRouter()

class Esp32Payload(BaseModel):
    temperatura: float
    umidade: float
    potenciometro: int
    gasAO: int
    gasDO: int
    alarme: str


@router.post("/")
def receber_dados(sensor: Esp32Payload):
    registros = completar_registros_esp32(sensor.model_dump(), qtd=1)
    inserir_registros_esp32(registros)

    resultado = pontuar_pulso(registros[0])

    return {
        "status": "ok",
        "dados_recebidos": sensor.model_dump(),
        "pontuacao": resultado
    }

@router.get("/kpis")
def get_kpis():
    try:
        return kpis_overview()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/kpis/maquina/{id_maquina}")
def get_kpis_maquina(id_maquina: int):
    try:
        return kpis_da_maquina(id_maquina)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/kpis/operador/{id_operador}")
def get_kpis_operador(id_operador: int):
    try:
        return kpis_do_operador(id_operador)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
