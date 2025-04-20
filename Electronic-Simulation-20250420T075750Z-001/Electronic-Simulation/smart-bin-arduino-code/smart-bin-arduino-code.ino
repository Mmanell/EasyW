const int voltagePin = A0;     // Voltage sensor pin
const int relayPin = 8;        // Relay control pin 
const int ledPin = 7;          // LED pin to indicate charging

// Define threshold voltage (example: 7.5V converted to analog value)
// If using a voltage divider, adjust accordingly
const float voltageThreshold = 7.5;
const float referenceVoltage = 5.0;
const int analogMax = 1023;

// Voltage divider values (if used)
const float R1 = 10000.0; // Top resistor
const float R2 = 4700.0;  // Bottom resistor

void setup() {
  pinMode(relayPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int rawValue = analogRead(voltagePin);

  // Convert analog reading to actual voltage using voltage divider formula
  float vIn = (rawValue * referenceVoltage / analogMax) * ((R1 + R2) / R2);

  Serial.print("Input Voltage: ");
  Serial.println(vIn);

  // Check if voltage is above threshold
  if (vIn > voltageThreshold) {
    digitalWrite(relayPin, HIGH); // Turn ON relay
    digitalWrite(ledPin, HIGH);   // LED ON
  } else {
    digitalWrite(relayPin, LOW);  // Turn OFF relay
    digitalWrite(ledPin, LOW);    // LED OFF
  }

  delay(1000); // Delay 1s between checks
}
