# Create AWS IoT Thing using python and boto3

This project will create things on AWS IoT platform using boto3 and python and download the certificates.

## Requirements

* AWS IAM User needs to have the permission for `AWSIoTFullAccess` and `AWSIoTDataAccess`

* Create a policy named `policy1`

* After installing AWS CLI, then you can use it to configure your credentials file:

      aws configure

  if don't you can create a credentials by creating credentials file under `~/.aws/` (`~/.aws/credentials`) and put:
  
      aws_access_key_id = YOUR_ACCESS_KEY
      aws_secret_access_key = YOUR_SECRET_KEY
      
* Install Boto3.  You can find more information about Boto3 [here](https://boto3.readthedocs.io/en/latest/guide/quickstart.html#installation)

* Change `defaultPolicyName`, `thingGroupName`, `thingGroupArn` values in source code to your appropriate ones.

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