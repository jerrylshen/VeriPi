#include <SPI.h>
#include <Wire.h>

#define LED 3
const int ledBool = false; 

void setup() {
  Serial.begin(9600);
  while (Serial.available()>0) 
  {
    serIn=Serial.read();
    
    if (serIn == "test")
    {
      pinMode(LED, OUTPUT);
      digitalWrite(LED, HIGH);
    }
  }

}

void loop() {

}
