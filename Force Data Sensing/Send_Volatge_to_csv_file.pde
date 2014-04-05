import processing.serial.*;
import java.util.*;
import java.text.*;

PrintWriter output;
DateFormat fnameFormat= new SimpleDateFormat("yyMMdd_HHmm");
DateFormat  timeFormat = new SimpleDateFormat("hh:mm:ss");
String fileName;

Serial myPort;  // Create object from Serial class
// Create object from Serial class
short portIndex = 2;

void setup() 
{
  //size(600, 600);
  String portName = Serial.list()[portIndex];
  myPort = new Serial(this, portName, 9600);
  Date now = new Date();
  fileName = fnameFormat.format(now);
  output = createWriter(fileName + ".csv"); // save the file in the sketch folder
}

void draw() {
  String timeString = timeFormat.format(new Date());
  
  char inByte = myPort.readChar();
  if(myPort.available() > 0 && inByte == 'f') {
    //output.println(timeString);
    println(timeString);
    //char inByte = myPort.readChar();
    //if(inByte == 'f') {
      // we expect data with this format f:XXXX
      
      myPort.readChar(); // discard ':'
      byte [] inData = new byte[4];
      myPort.readBytes(inData);
      
      int intbit = 0;
      
      intbit = (inData[3] << 24) | ((inData[2] & 0xff) << 16) | ((inData[1] & 0xff) << 8) | (inData[0] & 0xff);
      
      float f = Float.intBitsToFloat(intbit);
      println(f);
      output.println(f);
   /* }
    else{
      println();
    
    }*/
  }
}

void keyPressed() {
  println("pressed");
  output.flush(); // Writes the remaining data to the file
  output.close(); // Finishes the file
  exit(); // Stops the program
}
