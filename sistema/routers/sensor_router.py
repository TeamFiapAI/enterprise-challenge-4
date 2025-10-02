from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel
from datetime import datetime
from repository.oracle import salvar_dados_wokwi, salvar_predicao

router = APIRouter()

class SensorData(BaseModel):
    chuva_mm: float
    umidade: float
    pressao: float

class DadosPrevisao(BaseModel):
    PRECIPITACAO_TOTAL_DIARIO_mm: float
    TEMPERATURA_MEDIA_DIARIA_C: float
    UMIDADE_RELATIVA_DO_AR_MEDIA_DIARIA_pct: float    

class PrevisaoRequest(BaseModel):
    precipitacao_mm: float
    temperatura_maxima_c: float
    temperatura_minima_c: float
    temperatura_media_c: float
    temperatura_compensada_c: float
    umidade_media_pct: float
    umidade_minima_pct: float
    evaporacao_mm: float
    insolacao_horas: float
    vento_velocidade_ms: float
    pressao_hpa: float
    umidade_solo_pct: float

def prever_enchente(chuva_mm, umidade, pressao) -> str:
    if chuva_mm > 70 and umidade > 80 and pressao < 1000:
        return "EVACUAR"
    elif chuva_mm > 40:
        return "ALERTA"
    else:
        return "SEGURO"



@router.post("/")
def receber_dados(sensor: SensorData):
    print(f"Dados recebidos: {sensor}")
    status = prever_enchente(sensor.chuva_mm, sensor.umidade, sensor.pressao)
    return {
        "status": status,
        "dados_recebidos": sensor.dict()
    }



def request_to_model_input(req: PrevisaoRequest) -> dict:
    return {
        "precipitacao_mm": req.precipitacao_mm,
        "temp_max_c": req.temperatura_maxima_c,
        "temp_min_c": req.temperatura_minima_c,
        "temp_media_c": req.temperatura_media_c,
        "temp_compensada_c": req.temperatura_compensada_c,
        "umidade_media_pct": req.umidade_media_pct,
        "umidade_min_pct": req.umidade_minima_pct,
        "evaporacao_mm": req.evaporacao_mm,
        "insolacao_h": req.insolacao_horas,
        "vento_vel_media_ms": req.vento_velocidade_ms,
        "pressao_hpa": req.pressao_hpa,
        "umidade_solo_pct": req.umidade_solo_pct
    }

