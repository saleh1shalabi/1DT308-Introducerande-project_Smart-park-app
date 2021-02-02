import pycom
import time

pycom.rgbled(0x7f0000)
time.sleep(2)
pycom.rgbled(0x007f7f)
