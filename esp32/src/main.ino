#include <DHT.h>
#include <WiFi.h>
#include <LiquidCrystal_I2C.h>
#include <HTTPClient.h>

// DHT22 (sensor de temperatura e umidade)
#define DHTYPE DHT22
#define DHT_PIN 21     
DHT dht(DHT_PIN, DHTYPE);

#define POT_PIN 34         // Potenciômetro (simulando energia)
#define MQ2_PIN_D 33       // Saída digital do sensor MQ-2
#define MQ2_PIN_A 32       // Saída analógica do sensor MQ-2

#define BUZ_PIN 22         // Alarme sonoro
#define LED_PIN 23         // LED

LiquidCrystal_I2C lcd(0x27, 16, 2);
#define WIFI_SSID "Wokwi-GUEST"
#define WIFI_PASSWORD ""
#define SERVER_URL "http://192.168.0.107:8000/dados/"

void conectarWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Conectando ao WiFi");

  int tentativas = 0;
  while (WiFi.status() != WL_CONNECTED && tentativas < 20) {
    delay(500);
    Serial.print(".");
    tentativas++;
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("WiFi conectado: " + WiFi.localIP().toString());
  } else {
    Serial.println("Falha ao conectar ao WiFi.");
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Falha WiFi");
    delay(2000);
    lcd.clear();
  }
}

void setup()
{
  Serial.begin(9600);
  
  dht.begin();
 
  conectarWiFi();

  pinMode(BUZ_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  pinMode(MQ2_PIN_D, INPUT);   // Configura entrada digital do MQ2
  pinMode(MQ2_PIN_A, INPUT);   // Configura entrada analógica do MQ2 (opcional)
}

void loop()
{
  int alarme = 0;
  float umidade = dht.readHumidity();        // Lê a umidade
  float temperatura = dht.readTemperature(); // Lê a temperatura
  int potenciometro = analogRead(POT_PIN);    // Leitura do potenciômetro (simulando gás)
  
  //https://docs.wokwi.com/pt-BR/parts/wokwi-mq2-gas-sensor
  int gasDO = digitalRead(MQ2_PIN_D);          // Leitura digital do MQ2
  int gasAO = analogRead(MQ2_PIN_A);           // Leitura analógica do MQ2 (corrigido)

  Serial.print("Umidade: ");
  Serial.print(umidade);
  Serial.print(" % | Temperatura: ");
  Serial.print(temperatura);
  Serial.print("C | Potenciometro: ");
  Serial.println(potenciometro);

  Serial.print("Gas (analogico): ");
  Serial.println(gasAO);

  Serial.print("Gas (digital): ");
  if (gasDO == HIGH) {
    Serial.println(" | Smoke: -");
  } else {
    Serial.println(" | Smoke: Detected!");
  }

  // Condições para acionar alarme
  if (umidade > 70 || temperatura > 40 || potenciometro > 650 || gasDO == LOW) {
    digitalWrite(LED_PIN, HIGH);
    tone(BUZ_PIN, 500);
    alarme = 1;
  } else {
    digitalWrite(LED_PIN, LOW);
    noTone(BUZ_PIN);
    alarme = 0;
  }

  /*
    CSV ou Integracao:
    01 = umidade
    02 = temperatura
    03 = potenciometro
    04 = gas Analogico
    05 = gas digital
    06 = alarme
  */
  String linha = String(umidade) + ";" +
                String(temperatura) + ";" +
                String(potenciometro) + ";" +
                String(gasAO) + ";" +
                String(gasDO) + ";" +
                String(alarme);

  Serial.println("--------------------------------------------------");
  Serial.println(linha);
  Serial.println("--------------------------------------------------");
  Serial.println("");


  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(SERVER_URL);
    http.addHeader("Content-Type", "application/json");

    String payload = "{";
    payload += "\"temperatura\":" + String(temperatura, 1) + ",";
    payload += "\"umidade\":" + String(umidade, 1) + ",";
    payload += "\"potenciometro\":" +  String(potenciometro) + ",";
    payload += "\"gasAO\":" + String(gasAO) + ",";
    payload += "\"gasDO\":" + String(gasDO) + ",";
    payload += "\"alarme\":\"" + String(alarme) + "\"";
    payload += "}";

    int httpResponseCode = http.POST(payload);
    Serial.println("POST enviado | Código HTTP: " + String(httpResponseCode));
    Serial.println("Payload: " + payload);

    http.end();
  }

  delay(5000);
}
