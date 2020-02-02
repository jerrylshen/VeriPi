#include <Wire.h>
#include <SPI.h>
#include <Adafruit_CAP1188.h>

#include "SparkFunLSM6DS3.h"
#include <math.h>

#include "rgb_lcd.h"
rgb_lcd lcd;
int colorR = 150;
int colorG = 150;
int colorB = 150;

#define CAP1188_SENSITIVITY 0x1F

// Reset Pin is used for I2C or SPI
#define CAP1188_RESET  9

// CS pin is used for software or hardware SPI
#define CAP1188_CS  10

// These are defined for software SPI, for hardware SPI, check your 
// board's SPI pins in the Arduino documentation
#define CAP1188_MOSI  11
#define CAP1188_MISO  12
#define CAP1188_CLK  13

// For I2C, connect SDA to your Arduino's SDA pin, SCL to SCL pin
// On UNO/Duemilanove/etc, SDA == Analog 4, SCL == Analog 5

// Use I2C, no reset pin!
Adafruit_CAP1188 cap = Adafruit_CAP1188();

// Or...Use I2C, with reset pin
//Adafruit_CAP1188 cap = Adafruit_CAP1188(CAP1188_RESET);

// Or... Hardware SPI, CS pin & reset pin 
// Adafruit_CAP1188 cap = Adafruit_CAP1188(CAP1188_CS, CAP1188_RESET);

// Or.. Software SPI: clock, miso, mosi, cs, reset
//Adafruit_CAP1188 cap = Adafruit_CAP1188(CAP1188_CLK, CAP1188_MISO, CAP1188_MOSI, CAP1188_CS, CAP1188_RESET);
uint32_t timer = millis();

LSM6DS3 myIMU; //Default constructor is I2C, addr 0x6B (accel)
int steps = 0;
double prev_x = 0;
double prev_y = 0;

int passcode[] = {1, 2, 4, 3};
//int max_value = 16;
int counter = 0;

#define LED 3
const int ledBool = false; 

int alarm = 0; //when accelerometer triggers

//button stuff
const int buttonPin = 7;     // the number of the pushbutton pin
int buttonState = 0;

int isExit = 1;

void setup() {
  Serial.begin(9600);

  pinMode(6, OUTPUT); //buzzer
  
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  lcd.setRGB(colorR, colorG, colorB);
  lcd.clear();
  //lcd.print("Welcome");

  // Initialize the sensor, if using i2c you can pass in the i2c address
  
  if (!cap.begin()) {
    while (1);
  }
  cap.writeRegister(CAP1188_SENSITIVITY, 0x2F);
  
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  
  pinMode(LED, OUTPUT);
  digitalWrite(LED, LOW);
  myIMU.begin();
  delay(100);
  /*
  while (1)
  {
    uint8_t touched = cap.touched();

    if (touched == 0) {
      // No touch detected
      return;
    }
    
    for (uint8_t i=0; i<8; i++) {
      if (touched & (1 << i)) {
        Serial.print("C"); Serial.print(i+1); Serial.print("\t");
      }
    }
    Serial.println();
    //delay(50);
  }
  */
  
}

void loop() {
  
  //acceleration checking
  while (!alarm) {
    
    if (millis() - timer > 1500) {
      
      //Serial.print("\nAccelerometer:\n");
      //Serial.print(" X = ");
      //Serial.println(myIMU.readFloatAccelX(), 4);
      //Serial.print(" Y = ");
      //Serial.println(myIMU.readFloatAccelY(), 4);
      
      double temp_x = myIMU.readFloatAccelX();
      double temp_y = myIMU.readFloatAccelY();
    
      double temp_root = pow(pow(temp_x, 2) + pow(temp_y, 2), 0.5);
      double prev_root = pow(pow(prev_x, 2) + pow(prev_y, 2), 0.5);
      
      //Serial.println(temp_root);
      //Serial.println(prev_root);
      
      if(fabs(temp_root - prev_root)  > 0.8)
      {
        steps++;
        prev_x = temp_x;
        prev_y = temp_y;
        Serial.println("ALARM");
        lcd.clear(); 
        lcd.setCursor(0,0); lcd.print("Who are you?");
        //lcd.setCursor(0,1); lcd.print("you???");
        digitalWrite(LED, HIGH);
        alarm = 1;
        digitalWrite(6, HIGH);
        delay(65);
        digitalWrite(6, LOW);
        //Serial.println("");
      }
      
    }
  }

 
  while (alarm) {
    
    int isCorrect = 1; //1=true, 0=false
    int attempts = 0;
     
    while (Serial.available()) 
    { 
      //Serial.println("PAST SERIAL");
      char serIn = Serial.read();
      Serial.println(serIn);

      //debugging
      buttonState = digitalRead(buttonPin);
      if (buttonState)
      {
        return;
      }
      
      //if facial recognition works and verified
      if (serIn == '1')
      {
        Serial.println("Verified");
        digitalWrite(LED, LOW);
        lcd.clear(); 
        lcd.setCursor(0,0); lcd.print("VERIFIED"); 
        delay(1000);
        return;
        break;
      }

      //empty
      if (serIn == '9')
      {
        setup();
        return;
      }
      
      //if facial recognition didn't work, passcode
      if (serIn == '0')
      {
        lcd.clear(); 
        lcd.setCursor(0,0); lcd.print("PASSCODE?");
        //Serial.println("SerIN0000000000");
        
        while (1) 
        {
                    
          if (attempts == 3)
          {
            lcd.clear(); 
            Serial.println("TEXT");
            lcd.setCursor(0,0); lcd.print("3 FAILED TRIES");
            lcd.setCursor(0,1); lcd.print("REPORTED");
            
            digitalWrite(6, HIGH);
            delay(20);
            digitalWrite(6, LOW);
            delay(20);
            digitalWrite(6, HIGH);
            delay(20);
            digitalWrite(6, LOW);
            delay(20);
            digitalWrite(6, HIGH);
            delay(20);
            digitalWrite(6, LOW);
            
            while(1)
              int p;
          }
          
          if (millis() - timer > 30000) 
          {
            Serial.println("TEXT");
            digitalWrite(6, HIGH);
            delay(20);
            digitalWrite(6, LOW);
            delay(20);
            digitalWrite(6, HIGH);
            delay(20);
            digitalWrite(6, LOW);
            delay(20);
            digitalWrite(6, HIGH);
            delay(20);
            digitalWrite(6, LOW);
            while(1)
              int p;
          }
          
          int total = 0;
          uint8_t touched = cap.touched();
        
          if (touched == 0) {
            // No touch detected
            continue;
          }
          
          for (uint8_t i=0; i<8; i++) {
            if (touched & (1 << i)) {
              //Serial.print("C"); Serial.print(i+1); Serial.print("\t");
              total = i + 1;
            }
          }
        
          if (total)
          {
            int button_pressed = total;
            lcd.setCursor(counter,1); lcd.print(String(button_pressed));
            
            if(passcode[counter] != button_pressed)
            {
              isCorrect = 0;
            }
            
            ++counter;
            //Serial.print(String(counter));
            total = 0;
            
          }
          
          if(counter == 4 && isCorrect)
          {
            digitalWrite(LED, LOW);
            lcd.clear(); lcd.setCursor(0,0); lcd.print("Welcome!");
            counter = 0;
            alarm = 0;
            Serial.println("ENTRY");
            while(1)
              int p;
          }
  
          if (counter == 4 && !isCorrect)
          {
            counter = 0;
            lcd.clear();
            lcd.setCursor(0,0); lcd.print("WRONG");
            ++attempts;
          }
          //Serial.println();
          delay(600);
        } 
      }
    }
  }
}
