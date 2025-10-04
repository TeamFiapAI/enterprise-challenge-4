<p align="center">
<a href="https://www.fiap.com.br/">
<img src="./assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%">
</a>
</p>

![Arduino](https://img.shields.io/badge/arduino-3670A0?style=for-the-badge&logo=arduino&logoColor=ffdd54)
![C++](https://img.shields.io/badge/c++-3670A0?style=for-the-badge&logo=c%2B%2B&logoColor=ffdd54)
![PlatformIO](https://img.shields.io/badge/platformio-3670A0?style=for-the-badge&logo=platformio&logoColor=ffdd54)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Oracle](https://img.shields.io/badge/Oracle-3670A0?style=for-the-badge&logo=oracle&logoColor=ffdd54)

# Hermes Reply – Entrega 4 (MVP Integrado)
1. Coleta/ingestão de dados do ESP32/simulação (Wokwi/VSCode/PlatformIO);
2. Persistência no banco relacional modelado;
3. Treino e/ou inferência do modelo de ML básico;
4. Dashboard/relatório com KPIs e alertas (thresholds ou regra simples).


## 👨‍🎓 Integrantes
- Felipe Balthazar de Almeida
  - #RM562434
- Fernando Gomes da Silva
  - #RM561534
- Guilherme Urbinatti
  - #RM565203
- Vinicius Burchert Vilas Boas
  - #RM565395


## 🗂️ Estrutura de Pastas

```
📁/
├──📄README.md
|
├──📁assets/      
|
├──📁esp32/
│   ├──📄README.md
│   ├──diagram.json    → Formato JSON, que renderiza o Wokwi.
│   ├──libraries.txt   → Bibliotecas utilizadas no projeto.
│   ├──📁src/
│   ├──   ├──main.ino  → Codigo C++ da placa ESP32.
|
├──📁sistema/
|   ├──📁config/       → informacoes de login e senha do BD
|
|   ├──📁dashboard/    →  📊 streamlit e seus graficos
|
|   ├──📁models        →  ml
|
|   ├──📁prediction    →  ml
|
|   ├──📁repository    → consultas oracle 
|
|   ├──📁routers       → rotas da api
|
|   ├──📁scripts       → scripts do banco (criar tabela, inserir, dropar)
|
|   ├──📁services      → regras para alimentar a base de dados / gerar mock
|
|   ├──main.py          → toda parte de python > 🖥️uvicorn
|   ├──requeriments.txt → dependencias do projeto
|   ├──start.py         → inicia o 🖥️uvicorn e 📊streamlit 

```

---

## 🔧 Como Executar
### SISTEMA (Python)

### Alterar
```
...\config\config.json
{
    "ORACLE_USER": "RM001122",
    "ORACLE_PASSWORD": "------",
    "ORACLE_DSN": "oracle.fiap.com.br:1521/ORCL"
}
```

```
Windows
 > python -m venv venv
 > venv\Scripts\activate
 > cd sistema
 > pip install -r requirements.txt
 > python start.py
```
![Comandos no Terminal](./assets/windows.png)

### Sistema Python e Modelo ML: http://localhost:8000/docs
![Servico em Python](./assets/swagger.png)

### DashBoard Streamlit: http://localhost:8501/
![DashBoard Streamlit](./assets/streamlit.png)

- Exemplo de grafico
![heatmap](./assets/heatmap.png)