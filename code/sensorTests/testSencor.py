from machine import Pin
import pycom
import time

sensor = Pin('P8', mode = Pin.IN )
pycom.heartbeat(False)
pycom.rgbled(0x007f00)
blocked = False
print('lets go')


def sensorCallback(argument):
    # global blocked
    # if blocked:
    #     return
    # blocked=True
    if argument.value() == 1:
        print('Something is blocking me.')
        pycom.rgbled(0x7f0000)
        time.sleep(2)

    # global blocked
    # # if not blocked:
    # #     return
    # blocked = False
    else:
        print('Yay! im free.')
        pycom.rgbled(0x007f00)

sensor.callback(Pin.IRQ_RISING or Pin.IRQ_FALLING, sensorCallback)
