# AWS IoT Client Device Simulator

This project will create docker container to simulate an AWS IoT Client Device.  basic_discovery.py will discovery AWS Greengrass Core Device.  After discovering the Core Device, the simulator can communicate with AWS IoT through AWS Core Device.

## Requirements

* Install Docker   
  Refer to [here](https://docs.docker.com/engine/install/) to install Docker Engine.

* Install Docker Compose  
  Refer to [here](https://docs.docker.com/compose/install/) to install Docker Compose.

* Edit Dockerfile   
  Change `vehicle_0` to appropriate name 

* Build Docker Image for Client Device Simulator   

      sudo docker build -t vehicle_0 .

* Run Docker Container

      sudo docker run -it --name vehicle_0_container vehicle_0 

Now you can run AWS Iot Client Device Inside Docker Container

## Discover AWS IoT Core Device

* Run basic_discovery.py with appropriate arguments

   example:  
   python basic_discovery.py --thing_name GreengrassClientDevice1 --topic 'clients/GreengrassClientDevice1/hello/world' --message 'Hello World From Cllient Device 1!' --ca_file AmazonRootCA1.pem --cert device1-cert.pem.crt --key private.key --region us-east-1 --verbosity Warn

## Run AWS IoT Client Device Simulator

* Change `default_aws_endpint_url`
* Change `default_device_cert_name`.  This must match the one inside `\certificates` directory
* Change `default_device_key_file_name`.  This must match the one inside `\certificates` directory
* Change `default_root_ca_name`.  This must match the one inside `\certificates` directory

* Run emulator_client.py

   python emulator_client.py

* Publish data
      After all MQTTClients are initialized and subscribe to "vehicle/emission/data" topic, it will ask "send now?" to publish. Hit s to publish vehicle data.

* Check from AWS Console     
  You can subscribe "vehicle/emission/data" topic at `AWS iot > MQTT test Client` to check if emulator_client.py is appropriately publishing.  AWS IoT Core Device needs to deploy [MQTT Bridge Component](https://docs.aws.amazon.com/greengrass/v2/developerguide/mqtt-bridge-component.html) to bridge between AWS IoT Client Devices and AWS IoT Cloud Core.

## References
emulator_client.py references the following source:    
* [base code from Professor Matthew Caesar](https://drive.google.com/file/d/14ijMcHnxDTTCNwe-G3DWfy0ZF1C-5pmX/view)

## License
This project is open-source and free to use under the MIT License.

## Author
KyoSook Shin (kyosook2@illinois.edu)