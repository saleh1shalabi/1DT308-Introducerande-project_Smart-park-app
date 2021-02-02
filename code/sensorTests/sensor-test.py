from machine import Pin
import time
#
#
LED_r = Pin("P6", mode=Pin.OUT)
LED_g = Pin("P11", mode=Pin.OUT)
x = 0

def sens(arg):
    global x
    print("HEJ")
    x= x+1
    print(x)

sensPin = Pin('P8', mode=Pin.IN)


sen_r = sensPin.callback(Pin.IRQ_RISING, sens)

while True:
    if not sen_r:
        LED_r.value(1)
        LED_g.value(0)
        time.sleep(1)
    else:
        LED_g.value(1)
        LED_r.value(0)
        time.sleep(10)



#
#
#
#
