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
src/
├── sistema/
├── simulador/
├── assets/
└── 
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
![alt text](./assets/windows.png)

### Sistema Python e Modelo ML: http://localhost:8000/docs
### DashBoard Streamlit: http://localhost:8501/