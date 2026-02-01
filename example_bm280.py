"""
Datasheet:
BME280:  https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf
TCS3472:  https://cdn-shop.adafruit.com/datasheets/TCS34725.pdf
"""

import os

from adafruit_platformdetect import Detector

detector = Detector()
print("CHIP ID", detector.chip.id)


# FORCE BOARD AND CHIP

# os.environ['BLINKA_FORCECHIP'] = 'BCM2XXX'
os.environ['BLINKA_FORCEBOARD'] = 'RASPBERRY_PI_2B'

import board
from adafruit_bme280 import basic

# import adafruit_tcs34725

# Initialiser I2C
i2c = board.I2C()

# Initialiser les capteurs
bme280 = basic.Adafruit_BME280_I2C(i2c) # 0x77)

# Lecture des données
print(f"Température: {bme280.temperature:.1f}°C")
print(f"Humidité: {bme280.humidity:.1f}%")
print(f"Pression: {bme280.pressure:.1f}hPa")
