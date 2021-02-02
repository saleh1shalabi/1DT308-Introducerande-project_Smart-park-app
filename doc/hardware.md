# Hardware and hardware setup 

* LoPy 4
* Antenna
* RCWL-5016
* 9 V powersource
* 2 Leds
* 2 buttons
* 2 1K ohm pulldownresistor

## Explanations

The two leds will be used to indicate if the device is meant to be placed on the in-lane or on the out-lane. The device is placed in the middle of the drivinglane, its range is hopefully short enough so that something detected can be assumed to be a car driving on the in-lane --> +1 car on the parkinglot. One of the buttons is to swich between these two modes. The other button is to start and stop the process of detecting cars and sending data.The sensor has a 360 degree detection range radar that sends out microwaves and measures potential differenses in the returning wavelengths to determine movement. 

## Setup

<img src="img/Kopplingsschema.jpg" alt="koppligsschema" width="700"/>

Each component is connected with cables here represented by "<-->".

#### OUT-LED
* LoPy4 P12 <--> LED <--> resistor <--> LoPy4 GND

#### IN-LED
* LoPy4 P11 <--> LED <--> resistor <--> LoPy4 GND

#### Start/stop button
* LoPy4 P9 <--> Button <--> resistor <--> LoPy4 GND
* Button <--> LoPy4 3V3

#### Button switch
* LoPy4 P8 <--> Button <--> resistor <--> LoPy4 GND
* Button <--> LoPy4 3V3

#### RCWL-5016
* LoPy4 VIN(can be used as 5V powersource) <--> RCWL-5016 VIN
* RCWL-5016 output <--> LoPy4 P6
* RCWL-5016 GND <--> LoPy4 GND

#### Antenna
* Directly connected to either of LoPy4's LoRa antennas.
