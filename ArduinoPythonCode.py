import time, serial
import mosquitto

def messageReceived(broker, obj, msg):
	global ser
	print(“Message “ + msg.topic “ containing: “ + msg.payload)
	if msg.payload ==‘ON’: ser.write(“1”)
	else : ser.write(“0”)


client = mosquitto.Mosquitto(“Lights”)
client.connect(“176.24.147.53”)
client.subscribe(“LightShow”)
client.on_message = messageReceived

ser = serial.Serial(“/dev/cu.usbmodem14611”,9600,timeout=2)

while True: client.loop()
