from network import LoRa
import ubinascii
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
print(ubinascii.hexlify(lora.mac()).decode("utf-8").upper()) # prints out the device ID
