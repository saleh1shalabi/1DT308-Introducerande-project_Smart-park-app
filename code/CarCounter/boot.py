# print('hello!')
# from network import LoRa
# import time
# import ubinascii
#import pycom
#
# pycom.heartbeat(False)
# print('doing stuff')
#
# # Initialise LoRa in LORAWAN mode.
# lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
#
# # Create an OTAA authentication parameters, change them to the provided credentials
# app_eui = ubinascii.unhexlify('70B3D57ED003994D')
# app_key = ubinascii.unhexlify('4AA67EB7A192720AEA1D5E8817428940')
#
# # Join a network using OTAA (Over the Air Activation)
# lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
#
# # Wait until the module has joined the network
# print('im going to wait now')
# while not lora.has_joined():
#     time.sleep(2.5)
#     pycom.rgbled(0x00007f)
#     time.sleep(2.5)
#     pycom.rgbled(0x7f0000)
# print('nu är jag uppkoplad')

#All cred går till Emelie Sveborn
#pycom.rgbled(0x7f0000)
from network import LoRa
import time

# Please pick the region that matches where you are using the device

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
# while not lora.has_joined():
#     time.sleep(2.5)
#     pycom.rgbled(0x00007f)
#     time.sleep(2.5)
#     pycom.rgbled(0x7f0000)
print('donne')

# while True:
#     s.send('Car_OUT')
#     print('out {}'.format(i))
#     i= i+1
#     time.sleep(5)
