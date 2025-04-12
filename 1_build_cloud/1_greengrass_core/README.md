# AWS GreenGrass Edge Network

This project outlines how to configure an **AWS Greegrass Core device** to build an AWS edge network.



## Getting Started

### 1. Prerequisites

- An AWS IAM User must have the following permissions:
  - `AWSIoTFullAccess` 
  - `AWSIoTDataAccess`

### 2. Install AWS IoT Greengrass Core on Raspberry Pi
  Follow the official [AWS documentation](https://docs.aws.amazon.com/greengrass/v2/developerguide/install-greengrass-core-v2.html) to install **Greengrass Core v2** on your Raspberry Pi.

  - Use **default settings** throughout the installation. 
  - Choose **Automatic Resource Provisioning**
  

### 3. Configure the AWS Greegrass Core device
Once the Greengrass Core software is installed on the RAspberry Pi, it must be properly configured.
Refer to this helpful [YouTube video](https://youtu.be/tN0DQlQy2kM?si=Z_Yuub4eNE10JxA-) for step-by-step guidance on configuration. 
  


### 4. Create IoT Things  
Proceed to the [2_create_client](../2_create_client/) directory to create and manage your IoT Things.
  


## Useful Python Scripts
Use the following scripts **only if you intend to reset or clean up all resources**.  
These will **delete everything** from AWS IoT Core and may require a full reinstallation.

- [delete_all.py](./delete_all.py) - Deletes all IoT resources. 
- [delete_clients.py](./delete_clients.py) - Deletes client-related configurations.
- [delete_things.py](./delete_things.py)  - Deletes registered IoT Things.


## Author
KyoSook Shin (kyosook2@illinois.edu)



## License
This project is open-source and available under the **MIT License**.  

