#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

#include "Pipeline.h"
#include "Classifier.h"

Adafruit_MPU6050 mpu;


void setup() {
  Serial.begin(115200);
  Serial.println("Started");

  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
}

void loop() {
  float ax, ay, az, gx, gy, gz;

  sensors_event_t a, g, temp;
  mpu.getEvent(&g, &a, &temp);

  ax = a.acceleration.x;
  ay = a.acceleration.y;
  az = a.acceleration.z;
  gx = g.gyro.x;
  gy = g.gyro.y;
  gz = g.gyro.z;

  // perform feature extraction
  float features[] = {ax, ay, az, gx, gy, gz};

  if (!pipeline.transform(features))
    return;

  // perform classification
  Serial.print("Predicted gesture: ");
  Serial.print(forest.predictLabel(pipeline.X));
  Serial.print(" (DSP: ");
  Serial.print(pipeline.latencyInMicros());
  Serial.print(" micros, Classifier: ");
  Serial.print(forest.latencyInMicros());
  Serial.println(" micros)");
}
