# Hermes Reply: Coleta de Dados com ESP32
![Arduino](https://img.shields.io/badge/arduino-3670A0?style=for-the-badge&logo=arduino&logoColor=ffdd54)
![C++](https://img.shields.io/badge/c++-3670A0?style=for-the-badge&logo=c%2B%2B&logoColor=ffdd54)
![PlatformIO](https://img.shields.io/badge/platformio-3670A0?style=for-the-badge&logo=platformio&logoColor=ffdd54)


## Objetivos
- Criar um circuito virtual com ESP32 e ao menos um sensor simulado;
- Programar a leitura do sensor dentro da plataforma de simulação;
- Registrar os dados lidos (via Monitor Serial, CSV ou textual);

## Requisitos Técnicos e Funcionais

- Indicação dos sensores virtuais utilizados e justificativa;
- Esquema básico do circuito elétrico (print da simulação);
- Explicação da leitura dos dados na simulação;
- Trecho representativo do código;
- Registro da simulação funcionando;


## 📦 Componentes e Sensores Virtuais Utilizados
| Componente            | Função                                                                 | Motivo da Escolha                                                                 |
|-----------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| DHT22                 | Sensor de temperatura e umidade                                        | Fornece dados precisos e confiáveis de temperatura e umidade                      |
| Potenciômetro         | Simula uma entrada analógica variável (como energia)        | Permite testar limiares analógicos de forma simples e controlável                 |
| MQ-2 (Gás)            | Sensor de fumaça/gás com saídas digital e analógica                    | Simula vazamentos de gás e fumaça, útil para testar o acionamento de alarmes      |
| LED Vermelho          | Indicador visual de alarme                                              | Representa visualmente situações de alerta                                        |
| Buzzer                | Alarme sonoro     


## 🔄 Funcionamento da Simulação

### 📥 Leitura dos Dados

Os dados são coletados da seguinte forma:

- DHT22: Lê temperatura e umidade com os métodos readTemperature() e readHumidity().
- Potenciômetro: Lido via pino analógico 34 com analogRead(), simulando uma entrada variável (ex: energia, intensidade de gás).
- MQ-2:
  - Saída digital (DOUT): Lida com digitalRead() no pino 33, indica se há gás/fumaça (nível lógico).
  - Saída analógica (AOUT): Lida com analogRead() no pino 32, fornece intensidade do gás.
- Os valores são impressos no monitor serial e formatados em linha estilo CSV com:
  umidade;temperatura;potenciometro;gas_analogico;gas_digital;alarme


### 🚨 Acionamento de Alarme

O sistema aciona o LED e o buzzer quando qualquer uma das seguintes condições é detectada:

- Umidade acima de 70%
- Temperatura acima de 40°C
- Potenciômetro acima de 650
- Sensor de gás (digital) detecta fumaça/gás (LOW)

### Formato da Saída - CSV
#### COLUNAS
~~~~
umidade;temperatura;potenciometro;gas_analogico;gas_digital;alarme
~~~~
#### EXEMPLO
~~~~
40.50;2.30;0;3628;0;1
0.00;-40.00;320;3650;0;1
0.00;-40.00;320;1202;1;0
60.50;17.70;320;843;1;0
72.00;17.70;320;843;1;1
49.00;43.20;320;843;1;1
35.50;19.80;320;843;1;0
34.50;19.80;697;843;1;1
34.50;19.80;576;843;1;0
~~~~

### Referencia
[Wokwi](https://wokwi.com/projects/433368210236612609)