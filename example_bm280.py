from adafruit_platformdetect import Detector
detector = Detector()
print("CHIP ID", detector.chip.id)


import os

os.environ['BLINKA_FORCEBOARD'] = 'RASPBERRY_PI_2B'
# os.environ['BLINKA_FORCECHIP'] = 'BCM2835'

import board
from adafruit_bme280 import basic
# import adafruit_tcs34725



# Initialiser I2C
i2c = board.I2C()

# Initialiser les capteurs
bme280 = basic.Adafruit_BME280_I2C(i2c) # 0x77)
#bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c) # https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf
# tcs = adafruit_tcs34725.TCS34725(i2c) # https://cdn-shop.adafruit.com/datasheets/TCS34725.pdf

# Lecture des données
print(f"Température: {bme280.temperature:.1f}°C")
print(f"Humidité: {bme280.humidity:.1f}%")
print(f"Pression: {bme280.pressure:.1f}hPa")
