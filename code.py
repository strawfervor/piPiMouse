import analogio
import digitalio
import time
import usb_hid
from adafruit_hid.mouse import Mouse
from board import *

#hid device init
m = Mouse(usb_hid.devices)
#setting pins
xAxis = analogio.AnalogIn(A1)
yAxis = analogio.AnalogIn(A0)
buttonLeft = digitalio.DigitalInOut(GP17)
buttonLeft.direction = digitalio.Direction.INPUT
buttonLeft.pull = digitalio.Pull.UP
#boolean value to prevent from multiple cliks when pressing button
buttonPressed = False

#button = Pin(17,Pin.IN, Pin.PULL_UP)
#m = Mouse(usb_hid.devices)

while True:
    #settings values
    xValueRaw = int(xAxis.value / 100) -325
    yValueRaw = int(yAxis.value / 100) -325
    buttonValue = not buttonLeft.value
    
    #removing low values to prevent mouse cursor from difting
    if xValueRaw > 10:
        xValue = int((xValueRaw * -1)/20)#dividing by 12 to set speed
    elif xValueRaw < -10:
        xValue = int((xValueRaw * -1)/20)
    else:
        xValue = 0
        
    if yValueRaw > 10:
        yValue = int((yValueRaw * -1)/20)
    elif yValueRaw < -10:
        yValue = int((yValueRaw * -1)/20)
    else:
        yValue = 0
    
    #moving mouse
    m.move(xValue, yValue, 0)
    
    #pressing left button
    if buttonValue and not buttonPressed:
        m.click(Mouse.LEFT_BUTTON)
        buttonPressed = True
    elif buttonPressed and not buttonValue:
        buttonPressed = False
    
    #debug info
    #print("X: " + str(xValue) + ", Y: " + str(yValue) + " -- button value: " + str(buttonValue))
    time.sleep(0.03)
