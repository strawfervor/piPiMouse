Joystick with built-in pull-up on SW, no extra resistors needed.

---

## 1. CircuitPython version (original)

### Prerequisites
- CircuitPython for Pico – [install guide](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython)
- `adafruit_hid` from [Adafruit CircuitPython Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle) – copy to `/lib` on the Pico
- Copy `code.py` from this repo to the root of the Pico drive

Plug in, it appears as USB mouse immediately.

---

## 2. C++ version (PlatformIO + Arduino)

Faster, no CircuitPython needed. Uses Earle Philhower RP2040 core with TinyUSB HID.

### Prerequisites
- VSCode + PlatformIO extension
- Raspberry Pi Pico

### Setup
1. Clone repo
2. Open folder in PlatformIO
3. PlatformIO will auto-install the correct platform from `platformio.ini`
