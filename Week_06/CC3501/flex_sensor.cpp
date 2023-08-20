#include <Arduino.h>

const int flexPin = A0; // Define the ADC pin for the flex sensor
const int resistorValue = 10000; // 10K resistor is used in the volltage divider

void setup() {
  Serial.begin(115200); // Initialize serial communication
  pinMode(flexPin, INPUT); // Set the flex sensor pin as an input
}

void loop() {
  int sensorValue = analogRead(flexPin); // Read the sensor value (0-4095)
  
  // Convert the sensor value to voltage using the voltage divider formula
  float voltage = (float)sensorValue / 4095.0 * 3.3; // voltage is suplied by the 3.3V pin

  // Print the voltage to the serial terminal
  Serial.print("Flex Sensor Voltage: ");
  Serial.print(voltage, 2); // Display voltage with 2 decimal places
  Serial.println(" V");

  delay(1000); // Wait for a second before reading again
}