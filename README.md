<p align="center">
<a href="https://www.fiap.com.br/">
<img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%">
</a>
</p>

# Hermes Reply – Entrega 4 (MVP Integrado)
1. Coleta/ingestão de dados do ESP32/simulação (Wokwi/VSCode/PlatformIO);
2. Persistência no banco relacional modelado;
3. Treino e/ou inferência do modelo de ML básico;
4. Dashboard/relatório com KPIs e alertas (thresholds ou regra simples).


## 👨‍🎓 Integrantes
- Fernando Gomes da Silva
- Felipe Balthazar de Almeida
- Guilherme Urbinatti
- Vinicius Burchert Vilas Boas



## 🗂️ Estrutura de Pastas

```
src/
├── sistema/
│   ├── main.py                # 🚀 Inicialização da API FastAPI
│   ├── prediction/            # 🧠 Modelo de ML e previsão
│   ├── services/              # ⚙️ Lógica de negócio
│   ├── routers/               # 🌐 Endpoints da API
│   ├── telegram_bot.py        # 📲 Integração com Telegram Bot
assets/
└── history_data.csv           # 📁 Base histórica de dados
```

---

## 🔧 Como Executar

Pré-requisitos:
- Python 3.10+
- Pip
- Ambiente virtual (recomendado)

```bash
# Clone o repositório
git clone 
cd global-solution

# Instale as dependências
pip install -r requirements.txt

# Execute a API
python -m sistema.main

# Acesse a documentação interativa
http://localhost:8000/docs
```
