# AWS GreenGrass Edge Network

This project is about configuring AWS Greegrass Core device to compose AWS edge network.

## How to Start

* AWS IAM User needs to have the permission for `AWSIoTFullAccess` and `AWSIoTDataAccess`

* Install `AWS IoT Greengrass Core` software to RaspberryPi  
  Refer to [here](https://docs.aws.amazon.com/greengrass/v2/developerguide/install-greengrass-core-v2.html) to install AWS IoT Greengrass Core.  
  - All of the settings are to be default. 
  - Use Automatic Resource Provisioning
  

* Configure `AWS Greegrass Core device`  
  After installing the AWS Greengrass core software to RaspberryPi, it's important to configure the Greengrass core device properly.  
  Refer to [this Youtube video](https://youtu.be/tN0DQlQy2kM?si=Z_Yuub4eNE10JxA-) to properly configure the Greengrass Core device.  


* Create Things  
  Go to [2_create_client](../2_create_client/)  


## Useful Python Files
These are useful python files to clean up clients, things, and all.  
Do not use these files unless you want to clean up everything.  
These are going to erase the AWS Iot Core database, and you may need to install everything again.  

[delete_all.py](./delete_all.py)  
[delete_clients.py](./delete_clients.py)  
[delete_things.py](./delete_things.py)  

## License
This project is open-source and free to use under the MIT License.  

## Author
KyoSook Shin (kyosook2@illinois.edu)  