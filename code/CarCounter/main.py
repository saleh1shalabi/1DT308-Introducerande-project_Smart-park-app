from machine import Pin
import time
import utime
import _thread
import socket
import struct
import pycom

#boolians to let me check what is going on at a given moment.
inLane = True
justStopped=False
blinking = False

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

#timestamps to check bouncing. Tame for car is needed when testing with a button
#instead of a sensor.
timeForLastSwitch = utime.ticks_ms()
timeForStartButton = utime.ticks_ms()
timeForCar = utime.ticks_ms()

inLaneLed = Pin('P11', mode=Pin.OUT)
outLaneLed = Pin('P12', mode=Pin.OUT)

startButton = Pin('P9',mode=Pin.IN, pull=None)
laneSwitchButton = Pin('P8', mode= Pin.IN, pull=None)
motionSensor = Pin('P6', mode=Pin.IN)
#----------------------------------------------------------------------
#Variables you might want to adjust

bounceTime = 100 # how much time must pass when checking for button bounce

#LIGHTS
blinkRepeat = 3 # how many times the lights will blink when the device starts or stops counting cars.
blinkTimeON = 0.2 # how long time the lights will be on when blinking
blinkTimeOFF = 0.5 # how long the lights will be off when blinking
timeON = 1 # how long the light will be on when indicating a switch

#-------------------------------------------------------------------------

print('starting')

#this function is called when the 'switch' button is pressed.
def laneSwitch(argument):

    global inLane
    global timeForLastSwitch
    global inLaneLed
    global outLaneLed
    global timeON


    if bounceCheck(timeForLastSwitch):
        return

    if inLane:
        inLaneLed.value(0)
        outLaneLed.value(1)
        print('I just swiched from in lane to out lane!')

    else:
        inLaneLed.value(1)
        outLaneLed.value(0)
        print('I just swiched from out lane to in lane!')
    time.sleep(timeON)
    inLaneLed.value(0)
    outLaneLed.value(0)
    inLane = not inLane
    timeForLastSwitch = utime.ticks_ms()

def startFunction(argument):

    global startButton
    global timeForStartButton
    global justStopped

    if bounceCheck(timeForStartButton):
        return

    timeForStartButton = utime.ticks_ms()

    #we will stop by holding in the start button. when we let it go, this will
    #trigger a new startFunction, unless we make it so we can check if we just
    #stopped.
    if justStopped:
        justStopped = False
        return

    startButton.callback(Pin.IRQ_FALLING, None)

    print('starting')
    _thread.start_new_thread(mainCarCountingFunction, ())
    _thread.start_new_thread(blinkLightsXTimes, ())


def stopFunction(argument):

    global startButton
    global timeForStartButton
    global motionSensor
    global justStopped
    #
    # if time.ticks_diff(utime.ticks_ms(), timeForStartButton) < 100:
    #     print('to soon probably a bounce')
    #     return
    print('stopFunction')
    timeForStartButton = utime.ticks_ms()

    #will stop the car counting if start button is held for five seconds.
    while startButton.value() == 1:

        if utime.ticks_diff(utime.ticks_ms(), timeForStartButton) > 5000:
            print('no more car')
            motionSensor.callback(Pin.IRQ_RISING, None)
            timeForStartButton = utime.ticks_ms()
            bothLights()
            startButton.callback(Pin.IRQ_FALLING, startFunction)
            justStopped=True

            return
    blinkLightsXTimes()



def mainCarCountingFunction():
    global motionSensor
    global startButton
    global timeForStartButton

    time.sleep(3)
    print('entering a loop')
    motionSensor.callback(Pin.IRQ_RISING, carDetected)
    startButton.callback(Pin.IRQ_RISING, stopFunction)


def carDetected(argument):
    global timeForCar

    #needed when using a button while testing
    if bounceCheck(timeForCar):
        return

    timeForCar = utime.ticks_ms()

    if inLane:
        print('Car detected going in')
        s.send('Car_IN')
    else:
        print('Car detected going out')
        s.send('Car_OUT')

#blinks light ineffinetley, battery draining
def blinkLights():
    global blinking
    global outLaneLed
    global inLaneLed

    blinking = True
    while blinking:
        if inLane:
            blinkThisLight(inLaneLed)
        else:
            blinkThisLight(outLaneLed)

def blinkLightsXTimes():
        global blinkRepeat
        global outLaneLed
        global inLaneLed


        for _ in range(blinkRepeat):
            if inLane:
                blinkThisLight(inLaneLed)
            else:
                blinkThisLight(outLaneLed)


def blinkThisLight(light):

        global blinkTimeON
        global blinkTimeOFF

        light.value(1)
        time.sleep(blinkTimeON)
        light.value(0)
        time.sleep(blinkTimeOFF)

def stopBlinking():
    global blinking
    blinking = False

def bothLights():
    global inLaneLed
    global outLaneLed
    global timeON

    inLaneLed.value(1)
    outLaneLed.value(1)
    time.sleep(timeON)
    inLaneLed.value(0)
    outLaneLed.value(0)

def bounceCheck(timeStamp):

    global bounceTime

    if time.ticks_diff(utime.ticks_ms(), timeForLastSwitch) < bounceTime:
        print('to soon probably a bounce')
        return True
    return False


print('after functions')


laneSwitchButton.callback(Pin.IRQ_FALLING, laneSwitch)
startButton.callback(Pin.IRQ_FALLING, startFunction)
