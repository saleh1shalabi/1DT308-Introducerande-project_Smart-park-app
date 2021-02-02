import paho.mqtt.client as mqtt
import time
from kivy.properties import Property



broker = 'io.adafruit.com'
port = 1883
topic_cars_tot = "saleh_shalabi/feeds/Cars_TOT"
topic_Places = "saleh_shalabi/feeds/Places"
username = 'saleh_shalabi'
password = 'aio_eTQR01nk0h3dknsfy28Y37iWfW7c'
check = False
client = mqtt.Client()
client.username_pw_set(username, password=password)
client.connect(broker, port)



def on_connect(client, userdata, flags, rc):

    global check
    if rc == 0:
        check = True
        client.subscribe(topic_cars_tot)
        client.subscribe(topic_Places)
    else: 
        check = False

    return check

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

client.on_connect = on_connect



Cars_TOT = Property(1)
Places = Property(1)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global Cars_TOT, Places
    if msg.topic == topic_cars_tot:
        Cars_TOT = msg.payload.decode()
    if msg.topic == topic_Places:
        Places = msg.payload.decode()
    return str(Cars_TOT), str(Places)
    
def publish(client):
    msg = "update"
    result = client.publish("saleh_shalabi/feeds/App", msg)
    status = result[0]
    while status != 0:
        result = client.publish("saleh_shalabi/feeds/App", msg)
       
    

        
client.on_message = on_message


def run():
    # the function that runs when app is started 

    publish(client)

    client.loop_start()

def Msg_S_U():
    # to update values
    return publish(client)

