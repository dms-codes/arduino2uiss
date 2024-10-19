#include <dht11.h>

#define DHT11_PIN 2  // Define the DHT11 data pin

dht11 DHT11;

void setup() {
  // Initialize the serial communication at 9600 baud rate
  Serial.begin(9600);
}

void loop() {
  // Read the DHT11 sensor data
  int chk = DHT11.read(DHT11_PIN);

  // Print a new line for better readability
  Serial.println();

  // Check if the sensor data is valid
  if (chk == DHTLIB_OK) {
    // Print humidity
    Serial.print("Humidity (%): ");
    Serial.println(DHT11.humidity, 2);

    // Print temperature in Celsius
    Serial.print("Temperature (C): ");
    Serial.println(DHT11.temperature, 2);
  } else {
    // Handle error case
    Serial.print("Error reading DHT11: ");
    Serial.println(chk);
  }

  // Wait for 4 seconds before the next reading
  delay(4000);
}
