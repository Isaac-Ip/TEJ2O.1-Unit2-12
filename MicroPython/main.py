"""
Created by: Isaac Ip
Created on: Oct 2025
This module is a Micro:bit MicroPython program
This program uses if, else statements with hardware.
"""

from microbit import *
import neopixel

from hcsr04 import HCSR04


# variables
sensor = HCSR04(trigger_pin=12, echo_pin=13)
distance = sensor.distance_cm()
neopixelStrip = neopixel.NeoPixel(pin16, 4)

# cleanup
display.clear()
neopixelStrip[0] = (0, 0, 0)
neopixelStrip[1] = (0, 0, 0)
neopixelStrip[2] = (0, 0, 0)
neopixelStrip[3] = (0, 0, 0)
neopixelStrip.show()
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        distanceToObject = sonar.distance_mm() / 10
        display.clear()
        if distanceToObject < 10:
            display.show(Image.NO)
            neopixelStrip[0] = (255, 0, 0)
            neopixelStrip[1] = (255, 0, 0)
            neopixelStrip[2] = (255, 0, 0)
            neopixelStrip[3] = (255, 0, 0)
        else:
            display.show(Image.YES)
            neopixelStrip[0] = (0, 128, 0)
            neopixelStrip[1] = (0, 128, 0)
            neopixelStrip[2] = (0, 128, 0)
            neopixelStrip[3] = (0, 128, 0)
