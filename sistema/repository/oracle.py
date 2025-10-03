import oracledb
import os
import json

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG_PATH = os.path.join(BASE_PATH, "config", "config.json")
SCRIPTS_PATH = os.path.join(BASE_PATH, "scripts")

with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

DB_USER = config["ORACLE_USER"]
DB_PASSWORD = config["ORACLE_PASSWORD"]
DB_DSN = config["ORACLE_DSN"]

CAMINHO_SCRIPT_DROP = os.path.join(SCRIPTS_PATH, "drop.sql")
CAMINHO_SCRIPT_DDL = os.path.join(SCRIPTS_PATH, "ddl.sql")
CAMINHO_SCRIPT_INSERT = os.path.join(SCRIPTS_PATH, "insert.sql")

def get_conn():
    connection = oracledb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        dsn=DB_DSN
    )
    return connection

def dropar_tabelas():
    print("\n=== Verificando necessidade de dropar tabelas ===")

    if not os.path.exists(CAMINHO_SCRIPT_DROP):
        print(f"Script não encontrado: '{CAMINHO_SCRIPT_DROP}'")
        return

    with open(CAMINHO_SCRIPT_DROP, "r", encoding="utf-8") as f:
        ddl = f.read()

    comandos = [cmd.strip() for cmd in ddl.split(";") if cmd.strip()]

    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cursor:
            for comando in comandos:
                try:
                    cursor.execute(comando)
                except oracledb.DatabaseError as e:
                    error, = e.args
                    if error.code == 942:  # Tabela não existe
                        print("Tabela inexistente. Ignorando exclusão.")
                    else:
                        print(f"Erro no DROP:\n{comando}\n→ {error.message}")
                        raise
            conn.commit()
            print("Comandos de DROP executados (ou ignorados onde necessário).")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro ao dropar tabelas: {e}")
    finally:
        if conn:
            conn.close()

def executar_ddl():
    print("\n=== Executando script DDL ===")

    if not os.path.exists(CAMINHO_SCRIPT_DDL):
        print(f"Script não encontrado: '{CAMINHO_SCRIPT_DDL}'")
        return

    with open(CAMINHO_SCRIPT_DDL, "r", encoding="utf-8") as f:
        ddl = f.read()

    comandos = [cmd.strip() for cmd in ddl.split(";") if cmd.strip()]

    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cursor:
            for comando in comandos:
                try:
                    cursor.execute(comando)
                except oracledb.DatabaseError as e:
                    error, = e.args
                    if error.code in [955, 2275]:  # Objeto existe ou constraint já criada
                        print("Objeto ou constraint já existe. Ignorando.")
                    else:
                        print(f"Erro no DDL:\n{comando}\n→ {error.message}")
                        raise
            conn.commit()
            print("Script DDL executado com sucesso.")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro ao executar DDL: {e}")
    finally:
        if conn:
            conn.close()

def executar_insert():
    print("\n=== Executando inserts ===")

    if not os.path.exists(CAMINHO_SCRIPT_INSERT):
        print(f"Script não encontrado: '{CAMINHO_SCRIPT_INSERT}'")
        return

    with open(CAMINHO_SCRIPT_INSERT, "r", encoding="utf-8") as f:
        inserts = f.read()

    comandos = [cmd.strip() for cmd in inserts.split(";") if cmd.strip()]

    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cursor:
            for comando in comandos:
                try:
                    cursor.execute(comando)
                    print(f"✅ INSERT executado:\n{comando}")
                except oracledb.DatabaseError as e:
                    error, = e.args
                    print(f"Erro no INSERT:\n{comando}\n→ {error.message}")
                    continue
            conn.commit()
            print("Todos os INSERTs foram processados.")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro ao executar inserts: {e}")
    finally:
        if conn:
            conn.close()

def salvar_registros_fakes(registros):
    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cursor:
            for r in registros:
                cursor.execute("""
                    INSERT INTO registros (
                        id_maquina, id_operador, data_coleta,
                        temperatura, umidade, potenciometro,
                        gasAO, gasDO, alarme
                    ) VALUES (:m, :o, :d, :t, :u, :p, :g, :gd, :a)
                """, m=r["id_maquina"], o=r["id_operador"], d=r["data_coleta"],
                     t=r["temperatura"], u=r["umidade"], p=r["potenciometro"],
                     g=r["gasAO"], gd=r["gasDO"], a=r["alarme"])

                if f:
                    operador_str = str(r["id_operador"]) if r["id_operador"] else "NULL"
                    sql_insert = (
                        f"INSERT INTO registros (id_maquina, id_operador, data_coleta, temperatura, umidade, "
                        f"potenciometro, gasAO, gasDO, alarme)\n"
                        f"VALUES ({r['id_maquina']}, {operador_str}, "
                        f"TO_TIMESTAMP('{r['data_coleta'].strftime('%Y-%m-%d %H:%M:%S')}', 'YYYY-MM-DD HH24:MI:SS'), "
                        f"{r['temperatura']}, {r['umidade']}, {r['potenciometro']}, {r['gasAO']}, {r['gasDO']}, {r['alarme']});\n"
                    )
                    f.write(sql_insert)

            conn.commit()
        print(f"{len(registros)} registros inseridos com sucesso!")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro ao salvar registros fakes: {e}")
        raise
    finally:
        if conn:
            conn.close()
        if f:
            f.close()

def inserir_registros_esp32(registros):
    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cursor:
            for r in registros:
                cursor.execute("""
                    INSERT INTO registros (
                        id_maquina, id_operador, data_coleta,
                        temperatura, umidade, potenciometro,
                        gasAO, gasDO, alarme
                    ) VALUES (:m, :o, :d, :t, :u, :p, :g, :gd, :a)
                """, m=r["id_maquina"], o=r["id_operador"], d=r["data_coleta"],
                     t=r["temperatura"], u=r["umidade"], p=r["potenciometro"],
                     g=r["gasAO"], gd=r["gasDO"], a=r["alarme"])
            conn.commit()
        print(f"{len(registros)} registros inseridos com sucesso!")
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Erro ao inserir registros: {e}")
        raise
    finally:
        if conn:
            conn.close()