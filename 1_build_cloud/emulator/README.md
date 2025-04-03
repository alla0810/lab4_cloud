# Device Simulator

This project uploads the certificates created from "createThing-Cert.py" to the AWS emulators and connects the emulators to the IoT core.

## Requirements

* Install `AWSIoTPythonSDK`

      pip install AWSIoTPythonSDK


## Getting Started

* Set up AWS CLI  
    Install the AWS CLI for Raspberry Pi.

      curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install

    AWS CLI is successfully installed if you can see the following when you type `aws --version` command  

      aws-cli/2.x.x Python/3.x.x Linux/aarch64

* Install boto3 inside venv

      python -m venv .venv
      source .venv/bin/activate      
      pip install boto3

* Clone the repository

      git clone https://github.com/alla0810/lab4_cloud

      cd to `./1_build_cloud` directory

* Make `certificates` directory    

      mkdir certificates


* Run it

      python createThing-Cert.py

## References
This implementation references the following sources:    
* [keivanK1/aws-create-thing-boto3.git](https://github.com/keivanK1/aws-create-thing-boto3.git)

## License
This project is open-source and free to use under the MIT License.

## Author
KyoSook Shin (kyosook2@illinois.edu)