#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char *ssid = "Etudiants";
const char *password = "ENSAJ2020";

ESP8266WebServer server(80);

const int ledRPin = 12; // Define the pin to which the LED is connected (NodeMCU D1 pin)
const int ledYPin = 13;
const int ledGPin = 15;

const int ledR1Pin = 16;
const int ledY2Pin = 5;  
const int ledG3Pin = 4;  

bool etat = true;

void setup() {
  pinMode(ledRPin, OUTPUT);
  pinMode(ledYPin, OUTPUT);
  pinMode(ledGPin, OUTPUT);
  
  digitalWrite(ledRPin, LOW);
  digitalWrite(ledYPin, LOW);
  digitalWrite(ledGPin, HIGH);

  pinMode(ledR1Pin, OUTPUT);
  pinMode(ledY2Pin, OUTPUT);
  pinMode(ledG3Pin, OUTPUT);
  
  digitalWrite(ledR1Pin, LOW);
  digitalWrite(ledY2Pin, LOW);
  digitalWrite(ledG3Pin, LOW);

  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
    
  // Define REST API endpoint to receive LED state from Nest.js server
  server.on("/setLedState", HTTP_GET, setLedState);

  server.begin();
}

void loop() {
  server.handleClient();

  if (etat) {
    digitalWrite(ledRPin, HIGH);digitalWrite(ledYPin, LOW);digitalWrite(ledGPin, LOW);digitalWrite(ledR1Pin, LOW);digitalWrite(ledY2Pin, LOW);digitalWrite(ledG3Pin, HIGH);
    delay(2000);
    digitalWrite(ledRPin, LOW); digitalWrite(ledG3Pin, LOW);
    digitalWrite(ledGPin, HIGH);digitalWrite(ledYPin, LOW);digitalWrite(ledR1Pin, HIGH);
    delay(2000);
    digitalWrite(ledGPin, LOW);digitalWrite(ledR1Pin, LOW);
    digitalWrite(ledYPin, HIGH);digitalWrite(ledY2Pin, HIGH);digitalWrite(ledRPin, LOW);
    delay(1000);
  } else {
   digitalWrite(ledGPin, LOW);
   digitalWrite(ledYPin, LOW);
   digitalWrite(ledRPin, LOW);
   digitalWrite(ledG3Pin, LOW);
   digitalWrite(ledY2Pin, LOW);
   digitalWrite(ledR1Pin, LOW);

  }
}

void setLedState() {
  if (server.arg("state") == "off") {
    etat = false;
  } else if (server.arg("state") == "on") {
    etat = true;
  }

  server.send(200, "text/plain", "LED state updated");
}
