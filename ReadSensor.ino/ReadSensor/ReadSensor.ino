#include <Arduino.h>

#define SAMPLES_PER_SECOND 10

int samples[SAMPLES_PER_SECOND];
int sampleIndex = 0;

// Comparison function for qsort
int compare(const void* a, const void* b) {
  int int_a = *((int*)a);
  int int_b = *((int*)b);

  if (int_a == int_b) return 0;
  else if (int_a < int_b) return -1;
  else return 1;
}

void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  // Generate a new sample
  samples[sampleIndex] = random(0, 1023);
  sampleIndex = (sampleIndex + 1) % SAMPLES_PER_SECOND;

  // If a second has passed, calculate the mean and median
  static unsigned long lastPrint = 0;
  if (millis() - lastPrint >= 1000) {
    lastPrint += 1000;

    // Calculate mean
    int sum = 0;
    for (int i = 0; i < SAMPLES_PER_SECOND; i++) {
      sum += samples[i];
    }
    float mean = (float)sum / SAMPLES_PER_SECOND;

    // Calculate median
    int sortedSamples[SAMPLES_PER_SECOND];
    memcpy(sortedSamples, samples, sizeof(samples));
    qsort(sortedSamples, SAMPLES_PER_SECOND, sizeof(int), compare);
    float median = sortedSamples[SAMPLES_PER_SECOND / 2]; // If SAMPLES_PER_SECOND is even, you might want to average the two middle elements

    // Print the results
    Serial.print("sensor_id=1&mean=");
    Serial.print(mean);
    Serial.print("&median=");
    Serial.println(median);
  }
}