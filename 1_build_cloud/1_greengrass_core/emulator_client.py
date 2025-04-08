# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json
import pandas as pd
import numpy as np
import logging
#logging.basicConfig(level=logging.DEBUG)
import os
import shutil


#TODO 1: modify the following parameters
#Starting and end index, modify this
device_st = 0
device_end = 1


#Path to the dataset, modify this
data_path = "./data/vehicle{}.csv"

cert_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cert")

#Path to your certificates, modify this
core_device_certificate_path = os.path.join(cert_dir, "thingCert.crt")
core_device_key_path = os.path.join(cert_dir, "privKey.key")
core_device_root_ca_path = os.path.join(cert_dir, "rootCA.pem")

def copy_certificates():
    # Path to the source and destination directories
    source_cert_dir = "/greengrass/v2/"
    dest_cert_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cert")

    # List of the required certificate files
    cert_files = ["privKey.key", "thingCert.crt", "rootCA.pem"]

    # Ensure the destination directory exists
    if not os.path.exists(dest_cert_dir):
        os.mkdir(dest_cert_dir)

    # Copy certificate files from /greengrass/v2/ to cert directory
    for cert_file in cert_files:
        source_file_path = os.path.join(source_cert_dir, cert_file)
        dest_file_path = os.path.join(dest_cert_dir, cert_file)

        if os.path.exists(source_file_path):
            try:
                # Check if the file is readable
                if not os.access(source_file_path, os.R_OK):
                    print(f"Error: {cert_file} is not readable.")
                    continue

                # Attempt to copy the file
                shutil.copy(source_file_path, dest_file_path)
                print(f"Successfully copied {cert_file} to {dest_cert_dir}")

            except PermissionError:
                print(f"PermissionError: Unable to access {cert_file} from {source_cert_dir}")
                print("Attempting to run with elevated privileges (sudo)...")

                # Try running with sudo if needed (e.g., using subprocess)
                import subprocess
                subprocess.run(["sudo", "python3", __file__])
                break

        else:
            print(f"Error: {cert_file} does not exist in {source_cert_dir}")
            

class MQTTClient:
    def __init__(self, device_id, cert, key):
        # For certificate based connection
        self.device_id = str(device_id)
        self.state = 0
        self.client = AWSIoTMQTTClient(self.device_id)
        #TODO 2: modify your broker address
        self.client.configureEndpoint("a2rf5cc3bhluy5-ats.iot.us-east-1.amazonaws.com", 8883)
        self.client.configureCredentials(core_device_root_ca_path, key, cert)
        self.client.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.client.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.client.configureConnectDisconnectTimeout(10)  # 10 sec
        self.client.configureMQTTOperationTimeout(5)  # 5 sec
        self.client.onMessage = self.customOnMessage
        

    def customOnMessage(self,message):
        #TODO 3: fill in the function to show your received message
        print("client {} received payload {} from topic {}".format(self.device_id, message.payload, message.topic))


    # Suback callback
    def customSubackCallback(self,mid, data):
        #You don't need to write anything here
        pass


    # Puback callback
    def customPubackCallback(self,mid):
        #You don't need to write anything here
        pass

    def subscribe(self, topic="vehicle/emission/data"):
        self.client.subscribeAsync(topic, 0, ackCallback=self.customSubackCallback)
        print(f"Device {self.device_id} subscribed to {topic}")


    def publish(self, topic="vehicle/emission/data"):
        # Load the vehicle's emission data from file
        df = pd.read_csv(data_path.format(self.device_id))

        for index, row in df.iterrows():
            payload = json.dumps(row.to_dict())

            # Publish to topic
            print(f"Device {self.device_id} publishing: {payload} to {topic}")
            self.client.publishAsync(topic, payload, 0, ackCallback=self.customPubackCallback)

            # Optional: simulate real-time data publishing
            time.sleep(0.1)

copy_certificates()

print("Loading vehicle data...")
vehicle_data = []
for i in range(5):
    a = pd.read_csv(data_path.format(i))
    vehicle_data.append(a)

print("Initializing MQTTClients...")
clients = []
for device_id in range(device_st, device_end):
    client = MQTTClient(device_id,core_device_certificate_path ,core_device_key_path)
    client.client.connect()
    client.subscribe("vehicle/emission/data")
    clients.append(client)
 

while True:
    print("send now?")
    x = input()
    if x == "s":
        for i,c in enumerate(clients):
            c.publish()

    elif x == "d":
        for c in clients:
            c.client.disconnect()
        print("All devices disconnected")
        exit()
    else:
        print("wrong key pressed")

    time.sleep(3)