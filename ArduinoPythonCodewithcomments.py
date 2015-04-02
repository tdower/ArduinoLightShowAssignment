#Import required libraries or modules
import time, serial
import mosquitto

#The arduino receives the message whether to turn the led on, indicated by 1, or off, indicated by 0
def messageReceived(broker, obj, msg):
	global ser
	print(“Message “ + msg.topic “ containing: “ + msg.payload)
	if msg.payload ==‘ON’: ser.write(“1”)
	else : ser.write(“0”)

#Connects to the local IP of my computer ~176.24.147.53, then when the arduino has connected to the server it receives the message
client = mosquitto.Mosquitto(“TierneyD”)
client.connect(“176.24.147.53”)
client.subscribe(“LightShow”)
client.on_message = messageReceived

#Links to the arduino device and finds the seriel port and number of the arduino device 
ser = serial.Serial(“/dev/cu.usbmodem14611”,9600,timeout=2)

while True: client.loop()
