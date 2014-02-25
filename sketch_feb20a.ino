//From the article: http://bildr.org/2012/11/force-sensitive-resistor-arduino

int FSR_Pin = A0; //analog pin 0

void setup(){
  Serial.begin(9600);
}

void loop(){
  float FSRReading = analogRead(FSR_Pin)*(5.0/1023.0); 
  //float voltage = FSRReading*(5.0/1023.0);

  Serial.println(FSRReading);
  //Serial.println(voltage);
  delay(250); //just here to slow down the output for easier reading
}
