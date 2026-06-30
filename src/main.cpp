#include <Arduino.h>
#include "Mouse.h"

// PIN definitions
constexpr uint8_t PIN_X = 27; // GP27 (A1)
constexpr uint8_t PIN_Y = 28; // GP28 (A0)
constexpr uint8_t PIN_BTN = 17; // SW

bool buttonPressed = false;

void setup() {
  analogReadResolution(12);
  pinMode(PIN_BTN, INPUT_PULLUP);
  Mouse.begin();
}

void loop() {
  int xRaw16 = analogRead(PIN_X) * 16;
  int yRaw16 = analogRead(PIN_Y) * 16;

  int xValueRaw = (xRaw16 / 100) - 325;
  int yValueRaw = (yRaw16 / 100) - 325;

  bool buttonValue =!digitalRead(PIN_BTN);

  int xValue = 0, yValue = 0;

  if (xValueRaw > 10 || xValueRaw < -10) {
    xValue = (xValueRaw * -1) / 20; // /20 - speed, lower number to make it faster
  }
  if (yValueRaw > 10 || yValueRaw < -10) {
    yValue = (yValueRaw * -1) / 20;
  }

  if (xValue!= 0 || yValue!= 0) {
    Mouse.move(xValue, yValue, 0);
  }

  if (buttonValue &&!buttonPressed) {
    Mouse.press(MOUSE_LEFT);
    buttonPressed = true;
  } else if (!buttonValue && buttonPressed) {
    Mouse.release(MOUSE_LEFT);
    buttonPressed = false;
  }

  delay(30);
}