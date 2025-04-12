# Create AWS IoT Thing using python and boto3

This project automates the creation of AWS IoT Things using **Python** and **boto3**, and downloads associated certificates for use with AWS IoT Core.

## Requirements

### 1. Set up AWS CLI  
Install the AWS CLI on Raspberry Pi:

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Verify installation
```
aws --version
```

Expected output (version may vary):

```
aws-cli/2.x.x Python/3.x.x Linux/aarch64
```

### 2. Configure AWS Credentials
You can configure AWS credentials in one of two ways:  
**Option A: Using the AWS CLI**
```
aws configure
```
**Option B: Manually editing the redentials file**
Edit ~/.aws/credentials:

```  
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```
      
### 3. Install Boto3 in a Virtual Environment  
```
python -m venv .venv  
source .venv/bin/activate      
pip install boto3  
```      

Refer to [Boto3 documentation](https://boto3.readthedocs.io/en/latest/guide/quickstart.html#installation) for more details


## How to Run

### 1. Update the following variables in the source code (createThing-Cert.py) as needed:

* `defaultPolicyName1 = GreengrassV2IoTThingPolicy` 
* `defaultPolicyName2 = GreengrassTESCertificatePolicyGreengrassCoreTokenExchangeRoleAlias`  
* `thingGroupName = MyGreengrassCoreGroup` 
* `thingGroupArn = "YOUR_THING_GROUP_ARN"`

### 2. Run the script:
```
python createThing-Cert.py
```      

## 3. Copy generated certificates:
Copy the [certificates](./certificates/) directory to [3_emulator](../3_emulator/) directory

```
cp -r certificates ../3_emulator/
```

## References
This implementation references the following:    
* [keivanK1/aws-create-thing-boto3.git](https://github.com/keivanK1/aws-create-thing-boto3.git)


## Author
KyoSook Shin (kyosook2@illinois.edu)


## License
This project is open-source and free to use under the MIT License.

