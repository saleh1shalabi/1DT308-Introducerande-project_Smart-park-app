# Test

Take a lopy device and run the car_counter code. Press the 'switch' button: one of the LEDs should light up for a second to indicate witch mode is chosen, when the button is pressed again the other LED should light up. Press the buttons a few times and look at the terminal to see if there is bouncing. if the led changes again directly after a press the softwhere didnt succesfully identify a bounde. choose one LED. Press the start button, the chosen LED should blink three times. Set up a MQTT server with a feed to subscribe to. Now take another lopy and run the "main_device_code" code and alter authentication as needed, the MQTT should display a number that alter when the sensor is triggerd. Either adding or subtracting depending on the chosen LED. Test for both LED's. Look in the terminal of car_counter and see if it prints 'car going in' and 'car going out accordinly'.

When you run the main_device_code you can look in the terminal at the messages it is recieving. When the 'in-lane-mode' is chosen the message should be 'Car_IN', when the out-lane LED is chosen the message should be 'Car_OUT'. If you want to check witch mode is the current one, press the start button again and the LED corresponding to the current mode should blink three times. A message is sent each time the sensor detects movement. If you press the switch button the other led should blink three times and the message should change. When you want to stop sending messages and lisstening to the sensor hold the start button for about 10 seconds when both lights light up it means the car counting has stopped. if one LED blinks when you press the button, or after both leds lit up it is because of bouncing. Try holding the button again.

Tip!
If you want to have more control of when a message is sent, for testing, you could change the sensor for another button. Connect in the same manner as the other buttons. 