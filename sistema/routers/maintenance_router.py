from fastapi import APIRouter, HTTPException
from repository.oracle import dropar_tabelas, executar_ddl, executar_insert, salvar_registros_fakes
from services.logical_table import gerar_registros_fakes

router = APIRouter(prefix="/manutencao", tags=["Manutenção Tabelas"])

@router.post("/recriar-tabelas")
def recriar_base():
    try:
        dropar_tabelas()
        executar_ddl()
        return {"status": "ok", "mensagem": "Tabelas recriadas com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/popular-tabelas")
def popular_base():
    try:
        executar_insert()
        return {"status": "ok", "mensagem": "Tabelas populadas com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/fake")
def popular_base_fake():
    try:
        registros = gerar_registros_fakes(500)
        salvar_registros_fakes(registros, arquivo_sql="scripts/registros_mock.sql")
        return {"status": "ok", "mensagem": "Registros Criados com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
