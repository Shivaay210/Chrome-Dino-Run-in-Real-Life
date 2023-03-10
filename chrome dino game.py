#include <Keyboard.h>

int stretchThreshold = 990;
int forceThreshold = 1000;

void setup() {
  Keyboard.begin();
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int stretch = analogRead(A1);
  int force = analogRead(A2);

  Serial.print("stretch: ");
  Serial.print(stretch);
  Serial.print(" force: ");
  Serial.println(force);

  if(stretch < stretchThreshold){
    digitalWrite(LED_BUILTIN, HIGH);
    Keyboard.press(KEY_DOWN_ARROW);  
    delay(200);
    digitalWrite(LED_BUILTIN, LOW);
  }

  if(force < forceThreshold){
    digitalWrite(LED_BUILTIN, HIGH);
    Keyboard.press(' ');
    delay(200);  
    digitalWrite(LED_BUILTIN, LOW);
  }

  Keyboard.releaseAll();
}
