# Setup

## Components

* io.adafruit
    * feed - recieves data from main_device_code
* car_counter
    * main.py - buttons and LED's controlls, sends message to main device when sensor is triggerd, either Car_IN or Car_OUT
    * boot.py - connect to lora
* main_device_code
    * main.py - recives data from car_counter, uploads data to MQTT server, calculates the net sum of passing cars, conencts to lora, wifi and MQTT
    * boot.py - 
    * lib -  
* app
    * main.py - create the graphical interface the presents the collected data
    * connect.py - connects to MQTT

## Setup

### io.adafruit

The only setup needed is to change the authentications for the MQTT server and wifi. 

### car_counter

You might need to change the pin numbers to correspond with the pins you chose when setting up your hardware. If bouncing is going crazy you could try to adjust the variable "bounceTime". You can also adjust how the LEDs behave. Look for this part in the code: 

```{python}

#----------------------------------------------------------------------
#Variables you might want to adjust

bounceTime = 100 # how much time must pass when checking for button bounce

#LIGHTS
blinkRepeat = 3 # how many times the lights will blink when the device starts or stops counting cars.
blinkTimeON = 0.2 # how long time the lights will be on when blinking
blinkTimeOFF = 0.5 # how long the lights will be off when blinking
timeON = 1 # how long the light will be on when indicating a switch
#-------------------------------------------------------------------------
```

### main_device_code

Authentications for wifi connection will need to be changed to the proper one.
