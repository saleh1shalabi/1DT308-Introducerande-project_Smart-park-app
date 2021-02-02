import machine
import pycom
from network import LoRa
from network import WLAN
import socket
import time

from mqtt import MQTTClient


# lora to lora connect
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

time.sleep(2)




Cars_TOT = 0            # parked cars defult value
Places = 50             # availble places defult value
car_count = 0           # checker




wlan = WLAN(mode=WLAN.STA)

def wifi_connect():
    # connect to wifi
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect("LNU-iot", auth=(WLAN.WPA2, "modermodemet"), timeout=5000)

    while not wlan.isconnected():
        machine.idle()
    print("Connected to WiFi\n")



wifi_connect()




def sub_cb(topic, msg):
    global Cars_TOT, Places, car_count

    if msg == b"update": # when msg "update" publish values
        client.publish(topic="saleh_shalabi/feeds/Cars_TOT", msg=str(Cars_TOT))
        client.publish(topic="saleh_shalabi/feeds/Places", msg=str(Places))
    if topic == b"saleh_shalabi/feeds/reset_Cars":  # when msg gotten on reset car topic changes the values
        Cars_TOT = int(msg.decode("utf-8"))
        car_count = Cars_TOT

    if topic == b"saleh_shalabi/feeds/reset_Plac": # when msg gotten on reset places values
        Places = int(msg.decode("utf-8"))

    return Cars_TOT, Places, car_count







client = MQTTClient("lopy-saleh", "io.adafruit.com",user="saleh_shalabi", password="aio_eTQR01nk0h3dknsfy28Y37iWfW7c", port=1883)


client.set_callback(sub_cb)

client.connect()
client.subscribe(topic="saleh_shalabi/feeds/App")
client.subscribe(topic="saleh_shalabi/feeds/reset_Plac")
client.subscribe(topic="saleh_shalabi/feeds/reset_Cars")



print("mqtt connected")

while True:
    try:
        while not wlan.isconnected(): # if connection lost
            wifi_connect() # reconnect to wifi
            # re connect to mqtt server

            client.connect()
            client.subscribe(topic="saleh_shalabi/feeds/App")
            client.subscribe(topic="saleh_shalabi/feeds/reset_Plac")
            client.subscribe(topic="saleh_shalabi/feeds/reset_Cars")
            print("Conncetion lost, but istablished agane")
        else:
            client.check_msg() # check msg on mqtt


            if s.recv(64) == b'Car_IN':  # if a msg by lora from a device and its "Car_IN"
                print(s.recv(64))
                if Places == 0:         # check the values
                    print("where Are u going to park")
                else:                   # new values if there is places
                    Cars_TOT = Cars_TOT + 1
                    Places = Places - 1

            if s.recv(64) == b'Car_OUT':    #   if a msg by lora from a device and its "Car_OUT"
                print(s.recv(64))
                if Cars_TOT == 0:               # check values
                    print("how did this car even got in")
                else:                               # new values
                    Cars_TOT = Cars_TOT - 1
                    Places = Places + 1

            # check new values and publish it
            if Cars_TOT == (car_count +1):
                print("Cars + 1")
                client.publish(topic="saleh_shalabi/feeds/Cars_TOT", msg=str(Cars_TOT))
                client.publish(topic="saleh_shalabi/feeds/Places", msg=str(Places))
                car_count = car_count +1

            elif Cars_TOT == (car_count - 1):
                print("Cars - 1")
                client.publish(topic="saleh_shalabi/feeds/Cars_TOT", msg=str(Cars_TOT))
                client.publish(topic="saleh_shalabi/feeds/Places", msg=str(Places))
                car_count = car_count - 1

    except Exception as e:
        print(e)
