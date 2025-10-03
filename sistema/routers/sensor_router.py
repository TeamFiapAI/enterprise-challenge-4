from fastapi import APIRouter
from pydantic import BaseModel
from services.logical_table import gerar_registros_esp32
from repository.oracle import inserir_registros_esp32


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
    registros = gerar_registros_esp32(sensor.model_dump(), qtd=1)
    inserir_registros_esp32(registros)
    return {
        "status": "ok",
        "dados_recebidos": sensor.model_dump()
    }