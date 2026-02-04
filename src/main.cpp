#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <SparkFunTMP102.h>

TMP102 tempSensor;

//I2C address for raspberry pi (receiver)
#define PI_I2C_ADDRESS 0x08

void setup(){
  Serial.begin(9600);
  Wire.begin();
  if (!tempSensor.begin()){
    Serial.println("TMP102 not detected");
    while (1);
  }
  Serial.println("TMP102 connected");
}

void loop(){
  float temperature = tempSensor.readTempC();
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");
  delay(1000);
  Wire.beginTransmission(PI_I2C_ADDRESS);
  Wire.write((byte *)&temperature, sizeof(temperature));
  Wire.endTransmission();
  delay(1000);
}