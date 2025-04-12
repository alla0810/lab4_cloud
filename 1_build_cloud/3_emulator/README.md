# AWS IoT Client Device Simulator

This module provides a Docker-based simulator for an AWS IoT Client Device.  It uses   `basic_discovery.py` to discover an AWS Greengrass Core device, and then enables MQTT communication through the core device to AWS IoT Clouse.

## Requirements

### 1. Install Docker & Docker Compose
* [Install Docker Engine](https://docs.docker.com/engine/install/)

* [Install Docker Compose](https://docs.docker.com/compose/install/)

### 2. Prepare Dockerfile
* Open the [Dockerfile](./Dockerfile) and change `vehicle_0` to your preferred device name
  

### 3. Build Docker Image
```
sudo docker build -t vehicle_0 .
```      

### 4. Run Docker Container
```
sudo docker run -it --name vehicle_0_container vehicle_0 
```      
You now have a running IoT Client Device Simulator inside a Docker container.

### 5. Reconnect to Running Docker Container After Reboot or SSH Login
When you reconnect via SSH and want to resume working inside a running Docker container:

#### 1. List Running Docker Container
```
sudo docker ps
```

You will see output like:

````
CONTAINER ID   IMAGE       COMMAND       CREATED       STATUS        PORTS     NAMES
a1b2c3d4e5f6   vehicle_0   "/bin/bash"   2 hours ago   Up 2 hours              vehicle_0_container
````

#### 2. Enter the Running Container
Use the container name or ID from the list above:

```
sudo docker exec -it vehicle_0_container /bin/bash
```

This gives you an interactive shell inside the container.


## Discover Greengrass Core Device

Run basic_discovery.py with appropriate arguments to discover the AWS Greengrass Core:

```
(example)
python basic_discovery.py \
  --thing_name GreengrassClientDevice1 \
  --topic 'clients/GreengrassClientDevice1/hello/world' \
  --message 'Hello World from Client Device 1!' \
  --ca_file AmazonRootCA1.pem \
  --cert device1-cert.pem.crt \
  --key private.key \
  --region us-east-1 \
  --verbosity Warn

```   

* Refer to this helpful [Youtube video](https://youtu.be/tN0DQlQy2kM?si=Z_Yuub4eNE10JxA-) for configuring the Greengrass Core device.

## Run Client Device Simulator

### 1. Configure `emulator_client.py`
Make sure the following variables point to the correct files in your `\certificates` directory

* `default_aws_endpint_url`
* `default_device_cert_name`
* `default_device_key_file_name`
* `default_root_ca_name`

### 2. Run the Client Emulator
```
python emulator_client.py
```   

### 3. Publish data
Once all MQTT clients are initialized and subscribed to the topic `vehicle/emission/data`, the script will prompt:
```
send now? [s to publish]
```
Press `s` to publish simulated vehicle data to AWS IoT.

### 4. Verify on  AWS Console     
You can verify the data is being published via:  
**AWS IoT > MQTT Test Client > Subscribe to topic:**
```
vehicle/emission/data
```
The AWS Greengrass Core must have the [MQTT Bridge Component](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-bridge-component.html) deployed to bridge communication between edge devices and the cloud.

## References
emulator_client.py references the following source:    
* [Professor Matthew Caesar's IoT Project](https://drive.google.com/file/d/14ijMcHnxDTTCNwe-G3DWfy0ZF1C-5pmX/view)


## Author
KyoSook Shin (kyosook2@illinois.edu)


## License
This project is open-source and free to use under the MIT License.

