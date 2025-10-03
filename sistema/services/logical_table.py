import random
from datetime import datetime, timedelta

maquinas = [1, 2, 3, 4]
operadores = [1, 2, 3, 4]
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 1, 1)
delta_total = end_date - start_date

def gerar_registros_fakes(qtd=1000):
    """
    Gera uma lista de dicionários representando registros fakes,
    sem tocar no banco.
    """

    registros = []

    for _ in range(qtd):
        id_maquina = random.choice(maquinas)
        id_operador = random.choice(operadores)
        random_seconds = random.randint(0, int(delta_total.total_seconds()))
        data_coleta = start_date + timedelta(seconds=random_seconds)

        temperatura = round(random.gauss(25, 5), 2)
        umidade = round(random.gauss(40, 10), 2)
        potenciometro = random.randint(0, 4000)
        gasAO = random.randint(2000, 4000)
        gasDO = random.randint(0, 1)
        alarme = 1 if temperatura > 40 or gasAO > 3800 or gasDO == 1 else 0

        registros.append({
            "id_maquina": id_maquina,
            "id_operador": id_operador,
            "data_coleta": data_coleta,
            "temperatura": temperatura,
            "umidade": umidade,
            "potenciometro": potenciometro,
            "gasAO": gasAO,
            "gasDO": gasDO,
            "alarme": alarme
        })

    return registros

def gerar_registros_esp32(payload: dict, qtd: int = 1):
    registros = []

    for _ in range(qtd):
        id_maquina = random.choice(maquinas)
        id_operador = random.choice(operadores)
        random_seconds = random.randint(0, int(delta_total.total_seconds()))
        data_coleta = start_date + timedelta(seconds=random_seconds)

        temperatura = payload.get("temperatura", round(random.gauss(25,5),2))
        umidade = payload.get("umidade", round(random.gauss(40,10),2))
        potenciometro = payload.get("potenciometro", random.randint(0,4000))
        gasAO = payload.get("gasAO", random.randint(2000,4000))
        gasDO = payload.get("gasDO", random.randint(0,1))

        # Se o payload trouxe alarme, usa; se não, calcula
        alarme = int(payload.get("alarme")) if "alarme" in payload else (1 if temperatura > 40 or gasAO > 3800 or gasDO == 1 else 0)

        registros.append({
            "id_maquina": id_maquina,
            "id_operador": id_operador,
            "data_coleta": data_coleta,
            "temperatura": round(float(temperatura),2),
            "umidade": round(float(umidade),2),
            "potenciometro": int(potenciometro),
            "gasAO": int(gasAO),
            "gasDO": int(gasDO),
            "alarme": alarme
        })

    return registros