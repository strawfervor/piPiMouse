# piPiMouse
USB hid mouse using Raspberry Pi Pico and 5 pin analog joy stick

## Wiring
GND > GND
+5V > 3V3
VRX > GP27_A1
VRY > GP28_A0
SW  > GP17

## Prerequisites
- CircuitPython > [link to the source](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython)
- adafruit_hid from [CircuitPython libraries](https://github.com/adafruit/Adafruit_CircuitPython_Bundle) loaded in the "lib" folder of the Pico board
- From this repository, copy code.py into your Pico