/**
* Communicates float data over serial without loss of precision
*/

int state = LOW;
int FSR_Pin = A0;

void setup() {
  Serial.begin(9600); // setup serial connection speed
}

void loop() {
  float a = analogRead(FSR_Pin)*(5.0/1023.0);
  serialFloatPrint(a);

  delay(1000);
}


void serialFloatPrint(float f) {
  byte * b = (byte *) &f;
  Serial.print("f:");
  Serial.write(b[0]);
  Serial.write(b[1]);
  Serial.write(b[2]);
  Serial.write(b[3]);
  /* DEBUG */
  Serial.println();
  Serial.print(b[0],BIN);
  Serial.print(b[1], BIN);
  Serial.print(b[2], BIN);
  Serial.println(b[3], BIN);
  //*/
}
