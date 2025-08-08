import time
import paho.mqtt.client as mqtt
import ssl
import json
import _thread
from threading import Thread
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(21, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")


client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(ca_certs='./rootCA.pem', certfile='./blindtest-certificate.pem.crt', keyfile='./blindtest-private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("a72dr1evrf8dd-ats.iot.us-east-1.amazonaws.com", 8883, 60) #Taken from REST API endpoint - Use your own. 
client.on_message = on_message

"""
def intrusionDetector(Dummy):
    while (1):    
        #x=GPIO.input(21)
        x=0
        if (x==0): 
            print ("Just Awesome")
            client.publish("device/data", payload="Hello from BinaryUpdates!!" , qos=0, retain=False)
        time.sleep(5)

_thread.start_new_thread(intrusionDetector,("Create intrusion Thread",))
    """
    
client.loop_forever()