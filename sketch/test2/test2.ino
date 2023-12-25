#include <SPI.h>
#include <Wire.h>

// Define pins
const int pirPin = 8;
const int buzzerPin = 5;
const int ledPin = 4;

void setup() {
  pinMode(pirPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  // pinMode(cameraTriggerPin, OUTPUT);

  Serial.begin(9600); // Start serial communication
}

void loop() {
  int pirState = digitalRead(pirPin);

  if (pirState == HIGH) {
    tone(buzzerPin, 500, 5000);
    // digitalWrite(cameraTriggerPin, HIGH); // Trigger camera to take photo
    blinkLED(); // Blink LED

    // Send signal to external system for notification
    Serial.println("INTRUDER DETECTED");

    delay(1000); // Wait for 10 seconds before resetting
  } else {
    noTone(buzzerPin);
    digitalWrite(ledPin, LOW);
    // digitalWrite(cameraTriggerPin, LOW);
  }
}

void blinkLED() {
  for (int i = 0; i < 10; i++) {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
  }
}
