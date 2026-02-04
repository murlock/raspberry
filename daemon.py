import os
from time import time, sleep
import requests

# FORCE BOARD AND CHIP

# os.environ['BLINKA_FORCECHIP'] = 'BCM2XXX'
os.environ['BLINKA_FORCEBOARD'] = 'RASPBERRY_PI_2B'

import board
from adafruit_bme280 import basic
# import adafruit_tcs34725


VM_URL = "http://localhost:8428/api/v1/import/prometheus"
DELAY = 60 # en secondes


# Initialiser I2C
i2c = board.I2C()

# Initialiser les capteurs
bme280 = basic.Adafruit_BME280_I2C(i2c) # 0x77)

# Lecture des données
print(f"Température: {bme280.temperature:.1f}°C")
print(f"Humidité: {bme280.humidity:.1f}%")
print(f"Pression: {bme280.pressure:.1f}hPa")



def read_and_send() -> None:
    timestamp = int(time() * 1e3)
    metrics = f"""
    # TYPE bme280_temperature gauge
    bme280_temperature{{location="home"}} {bme280.temperature:.2f} {timestamp}

    # TYPE bme280_humidity gauge
    bme280_humidity{{location="home"}} {bme280.humidity:.2f} {timestamp}

    # TYPE bme280_pressure gauge
    bme280_pressure{{location="home"}} {bme280.pressure:.2f} {timestamp}
    """
    resp = requests.post(VM_URL, data=metrics.encode("utf-8"), timeout=(5.0, 5.0))
    print(timestamp, f"{bme280.temperature:.2f}", resp.status_code)

while True:
    read_and_send()
    sleep(DELAY)
