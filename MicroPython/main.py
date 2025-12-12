"""
Created by: Isaac Ip
Created on: Dec 2025
This module is a Micro:bit MicroPython program
This program uses if, else statements with hardware.
"""

from microbit import *
from machine import time_pulse_us
import neopixel

# variables and setup
trig = pin12
echo = pin13
trig.write_digital(0)
echo.read_digital()
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
        # Output a pulse to trigger ultrasonic burst
        trig.write_digital(1)
        trig.write_digital(0)

        # Measure the input echo pulse in microseconds, convert to seconds
        micros = time_pulse_us(echo, 1)
        t_echo = micros / 1000000
        # Calculate distance in cm and display on micro:bit
        dist_cm = (t_echo / 2) * 34300
        display.scroll(str(int(dist_cm)))
        if dist_cm < 10:
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
    neopixelStrip.show()
