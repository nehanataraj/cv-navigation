from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import json
import pygame
import io
import base64
#logging.basicConfig(level=logging.DEBUG)

# Replace with your AWS IoT Thing settings
iot_endpoint = "a72dr1evrf8dd.iot.us-east-1.amazonaws.com"
iot_ats_endpoint = "a72dr1evrf8dd-ats.iot.us-east-1.amazonaws.com"
root_ca_path = "/Users/shubha/Desktop/BlindProject/certs/AmazonRootCACorrect.cer"
private_key_path = "/Users/shubha/Desktop/BlindProject/certs/blindtest-private.pem.key"
certificate_path = "/Users/shubha/Desktop/BlindProject/certs/blindtest-certificate.pem.crt"
client_id = "your_client_id"

# Initialize the AWS IoT MQTT Client
mqtt_client = AWSIoTMQTTClient(client_id)
mqtt_client.configureEndpoint(iot_ats_endpoint, 8883)
mqtt_client.configureCredentials(root_ca_path, private_key_path, certificate_path)

# Callback function to handle incoming messages
def custom_callback(client, userdata, message):
    print(f"Received message on topic {message.topic}: {message.payload}")

# Replace with your audio playback settings
audio_output_device = "default"  # You may need to specify the audio device ID

# Initialize pygame mixer
pygame.mixer.init()

def custom_callback(client, userdata, message):
    try:
        # Decode the base64-encoded audio data
        audio_data = base64.b64decode(message.payload)

        # Play the audio using pygame
        play_audio(audio_data)
    except Exception as e:
        print(f"Error playing audio: {e}")

def play_audio(audio_data):
    # Load audio data into a pygame Sound object
    sound = pygame.mixer.Sound(io.BytesIO(audio_data))

    # Play the audio
    sound.play()

    # Set the callback function
#mqtt_client.setCallback(custom_callback)

# Connect to AWS IoT
try:
    mqtt_client.connect()
    print("Connected to AWS IoT")
except Exception as e:
    print(f"Error: {e}")

# Do your MQTT operations here...

# Subscribe to a topic
topic = "audiofile"
qos = 1  # Quality of Service (QoS) level
mqtt_client.subscribe(topic, qos, custom_callback)

# Publish message to an IoT topic
iot_topic = "testtopic"
message_payload = {"Hello": "there"}

# Convert the message payload to JSON format
message_json = json.dumps(message_payload)

# Publish the message
#mqtt_client.publish(iot_topic, message_json, 1)  # QoS 1

# Wait for the message to be published (optional)
time.sleep(2)
# Wait for incoming messages
while True:
    #mqtt_client.yieldCallback()
    time.sleep(1)

# Disconnect from AWS IoT
mqtt_client.disconnect()
print("Disconnected from AWS IoT")
