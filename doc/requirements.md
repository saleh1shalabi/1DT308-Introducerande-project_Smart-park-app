# Car counter

## Problem
Kalmar kommun has specified the following problem: Parkeringsplats, fullt eller inte fullt, antal lediga platser.

* People park for to long or without paying.
* The current way to count available parkingspaces does not work well.

___
## User stories
* *US1*: As a user I must be able to access information about how many cars has entered and exited the parkinglot since the device was placed.
* *US2*: As a user I could be able to enter the number of cars that are already on the parkinglot.
* *US3*: As a user I could be able to enter the total number of parkingspaces on the parkinglot.
* *US4*: As a user I could be able to see how many free spaces there are on a certain parkinglot.
___
## Device requierments

* *DR1*: The device must be portable and easy to set up.
* *DR2*: The device must be a selfcontained unit.
* *DR3*: The device must try to utilize the available sensors.
* *DR4*: The device must be safe to place.
* *DR5*: The device could use a magnetic sensor to further verify that is is a car and not something else.
---
## Breakdowns

### **User story breakdowns**

* **US1**
    * US11: When the device detects a car this information is saved and sent to a server.
    * US12: By subscribing to this server you can access the information about the number of cars that have entered or exited the parkinglot.

* **US2**
    * US21: The case of the device have buttons that make it possible to enter numbers.
    * US22: The case of the device has a little screen that ask the user to enter the number of cars. 
    * US23: The screen can show what number have been entered.
    * US24: The case of the device have an 'OK' or 'Enter' button wich the user can press to finish writing in the number.
    * US25: The entered number is sent to the server.


* **US3**
    * US31: See US21
    * US32: See US22
    * US33: See US23
    * US34: See US24
    * US35: See US25

* **US4**
    * US41: When the server recives in formation about the number of spaces it subtracts used spaces from total spaces.
    * US42: Each time a car exits or enters the available space change.


### **Device requirement breakdowns**

* **DR1**
    * DR11: The device must be relativley easy to move and carry.
    * DR12: A user should be able to carry the device in one hand.
    * Placing the device should be as simple as laying it on the ground or atatching it to a dedicated mount.

* **DR2**
    * DR21: A case should be designed that contains everything the device needs.
        * lopy 4
        * battery
        * Lora antenna
        * Sensors 
        * screen (if time permitts)
        * Buttons (if time permitts)
        * coil (if time permitts)
    
    * DR22: The case is designed to be 3D-printed.

* **DR3**
    * DR31: Different ways of utilising the RCWL-0516.
        * One device for each lane
        * Each time the sensor gives a signal it is counted as a car.
        * The direction of the car is determined based on wich lane the device is placed on.
    * DR32: Problems with the RCWL-0516.
        * The sensor 'looks' in all directions, so it will detect cars in other places than the lane it is placed on.
        * The sensor reacts to pedestrians.
        * The sensor seams unreliable. 
    * DR33: The sensor could be screened of to help with some of the problems.

    * DR34: Designing the device to be placed on the lane with the sensor facing uppwards could help with some of the problems.
        * Cars drive over the cevice.
        * Device must be flat and low to the ground.
        * Device must be highley vissible.
    * Adding the resistor that limits the sensors range from 7 meters to 5 meters could help with some of the problems.

* **DR4**
    * DR41: Placing the device must not involve spending unnescesery time on or in conection to the road.
    * DR42: While placing the device the user must be able to be highly vissible.
    * DR43: While placing the device the user must be able to keep their attention on their suroundings. 

* **DR5**
    * DR51: Different magnetic sensors that could be used:
        * digital hall sensor.
        * A coil (placed iside, around the edges of a round case)
    * DR52: When the RCWL-0516 sences something the magnetic sensor verifies that it is likely a car and not a pedestrian.
