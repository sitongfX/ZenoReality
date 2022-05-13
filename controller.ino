#include <ArduinoJson.h>

  uint8_t buttonVal = 1;
  int joyX = 1700;
  int joyY = 1700;
  int potVal = 0;

void setup() {
  Serial.begin(250000);
  delay(8000); // give me time to bring up serial monitor
  
  while (!Serial) continue;
  pinMode(15, INPUT_PULLUP);
  
}

// button - ground and pin 15, pressed as 0, normal as 1
// potentiometer pin 12
// joystick VRy(27)-white Vrx(26) black


void loop(){

  buttonVal = digitalRead(15); 
  joyX = map(analogRead(26), 0, 4096, 0, 100);
  joyY = map(analogRead(27), 0, 4096, 0, 100); 
  potVal = map(analogRead(12), 0, 4096, 0, 20);
  
  StaticJsonDocument<200> doc;

  doc["P"] = potVal;
  doc["X"] = joyX;
  doc["Y"] = joyY;
  doc["B"] = buttonVal;
  
  String s = "";
  serializeJson(doc, s);
  Serial.print(s);
  Serial.print("\n");  
}
