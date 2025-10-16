"""
Created by: Isaac Ip
Created on: Oct 2025
This module is a Micro:bit MicroPython program
This program uses if, else statements with hardware.
"""

from microbit import *
import neopixel


class HCSR04:

    def __init__(self, tpin=pin1, epin=pin2, spin=pin13):
        spi.init(
            baudrate=125000,
            sclk=self.sclk_pin,
            mosi=self.trigger_pin,
            miso=self.echo_pin,
        )

    def distance_mm(self):
        spi.init(
            baudrate=125000,
            sclk=self.sclk_pin,
            mosi=self.trigger_pin,
            miso=self.echo_pin,
        )
        pre = 0
        post = 0
        k = -1
        length = 500
        resp = bytearray(length)
        resp[0] = 0xFF
        spi.write_readinto(resp, resp)
        # find first non zero value
        try:
            i, value = next((ind, v) for ind, v in enumerate(resp) if v)
        except StopIteration:
            i = -1
        if i > 0:
            pre = bin(value).count("1")
            # find first non full high value afterwards
            try:
                k, value = next(
                    (ind, v)
                    for ind, v in enumerate(resp[i : length - 2])
                    if resp[i + ind + 1] == 0
                )
                post = bin(value).count("1") if k else 0
                k = k + i
            except StopIteration:
                i = -1
                dist = (
                    -1
                    if i < 0
                    else round(((pre + (k - i) * 8.0 + post) * 8 * 0.172) / 2)
                )
                return dist


sonar = HCSR04()

# variables
distanceToObject = 0
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
