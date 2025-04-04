# Device Simulator

This project initializes five AWS MQTT Clients that were created by running `createThing-Cert.py` and connects them to the AWS IoT core.  To check if the MQTT Clients have been successfully connected to the AWS core, they are subscribing to "vehicle/emission/data" topic, and publish data read from `vehicle[0].csv`~`vehicle[4].csv` files.

## Requirements

* Virtual Environment
      `emulator_client.py` should be run under virtual environment.

      python -m venv .venv  
      source .venv/bin/activate       

* Install `AWSIoTPythonSDK`

      pip install AWSIoTPythonSDK

* Install `panda`

      pip install pandas


## Getting Started

* run `createThin-Cert.py` first before running `emulator_client.py`  

* Directory Structure    
    To run `emulator_client.py`, keeping the directory structure is important.

    1. `createThings` directory and `emulator` directory need to be under the same path.  
    2. `data` directory needs to be under `emulator` directory.  
    3. `keys` directory needs to be under `emulator` directory.  
    4. `certificates` directory needs to be under `createThings` directory.  
        => `certificates` directory has been automatically created after running `createThing-Cert.py`.  Do not change this directory structure.  

* File names  
      1. `emulator_client.py` reads vehicle data from `./data/vehicle[0].csv`~`./data/vehicle[4].csv`.  Do not change these file names  
      2. `emulator_client.py` reads AWS Root key from `./keys/AmazonRootCA1.pem` file.  Download AWS Root key here, and rename it to `AmazonRootCA1.pem`  
      3. `emulator_client.py` uses certificates that were created when running `createThing-Cert.py`.  Do not change `../createThings/certificates` directory and the contents of it.  

* AWS Endpoint  
      Copy the AWS End Point and overwrite it to the `configureEndpoint(ENDPOINT)` part in line 32.


* How to run

      python emulator_client.py  

* Publish data  
      After all MQTTClients are initialized and subscribe to "vehicle/emission/data" topic, it will ask "send now?" to publish.  Hit `s` to publish vehicle data.


## References
This implementation references the following sources:    
* [base code from Professor Matthew Caesar](https://drive.google.com/file/d/14ijMcHnxDTTCNwe-G3DWfy0ZF1C-5pmX/view)

## License
This project is open-source and free to use under the MIT License.

## Author
KyoSook Shin (kyosook2@illinois.edu)