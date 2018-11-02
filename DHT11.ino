#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#include <Wire.h>

#define SLAVE_ADDRESS 0x04

#define FLOATS_SENT 4
int number =0;
float temperature = 0;
float luminosity = 0;
float shit=0;
float poop=0;
float data[FLOATS_SENT];
#define DHTPIN            2         // Pin which is connected to the DHT sensor.
#define PIN A0
#define DHTTYPE           DHT11     // DHT 11 
DHT_Unified dht(DHTPIN, DHTTYPE);
#define pingPin 8
#define echoPin 7
uint32_t delayMS;

void setup() {
  
  Serial.begin(9600);

    
    // initialize i2c as slave
    Wire.begin(SLAVE_ADDRESS);
    Wire.onReceive(receiveData);
    Wire.onRequest(sendData);
    Serial.println("Ready"); 
  sensor_t sensor;
  pinMode(PIN,INPUT);
  dht.temperature().getSensor(&sensor);
  dht.humidity().getSensor(&sensor);
  delayMS = sensor.min_delay / 1000;
}
float duration;
void loop() {
  delay(delayMS);
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(pingPin, LOW);
  pinMode(echoPin, INPUT);
  poop = pulseIn(echoPin, HIGH);
  sensors_event_t event;  
  dht.temperature().getEvent(&event);
  temperature=event.temperature;
  dht.humidity().getEvent(&event);
  luminosity=event.relative_humidity;
  shit=analogRead(PIN);

    data[0] = temperature;
    data[1] = luminosity;
    data[2]= shit;
    data[3]= poop;
}
void receiveData(int byteCount){
while(Wire.available()) {
number = Wire.read();
if(number!=0)
{
Serial.println("data received: ");
Serial.println(number);
}
}
}
void sendData(){
  Wire.write((byte*) &data, FLOATS_SENT*sizeof(float));
}
