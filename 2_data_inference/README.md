# Lab 4: Self-Driving Car Emission Data Processor

## Overview

This project demonstrates the use of AWS IoT and Greengrass to process and visualize emission data from self-driving vehicles. The application collects data from vehicles, processes CO₂ emissions, and publishes the results for visualization.

### Current Status

- **Step 1**: Setup AWS Greengrass Core. ✅
- **Step 2**: Processed vehicle emission data with a Greengrass component. ✅
- **Step 3**: *In Progress* – configuring **Firehose**, **Glue**, **Athena** for data visualization _(To be completed by another group member)_

---

## Components

- **Emissions Processor Component**: A custom AWS Greengrass component that subscribes to an MQTT topic, processes CO₂ data, and republishes the result.
- **Emulator Client**: A Python-based simulation tool that mimics vehicle telemetry and publishes real-time data to the MQTT broker.

---

## Prerequisites

Before starting, ensure you have the following:

- An **AWS Account** with IAM permissions for:
  - AWS IoT Core
  - Greengrass
  - S3
  - Firehose
  - Glue
  - Athena
- **Python 3.x**
- **AWS CLI** installed and configured
- **Git** installed
- **Raspberry Pi (or other Greengrass-compatible device)** set up with Greengrass v2

You also need to clone and use configuration files from Kyosook's project:

**➡ GitHub repo**: [https://github.com/alla0810/lab4_cloud](https://github.com/alla0810/lab4_cloud)

---

## Setup Instructions

### 1. Clone the Project Repositories

```bash  
git clone https://github.com/alla0810/lab4_cloud.git  
https://github.com/alla0810/lab4_cloud/tree/main/2_data_inference 
cd 2_data_inference   
```

---

### 2. Configure AWS CLI

```bash  
aws configure  
```

Provide your `Access Key`, `Secret Access Key`, `Region`, and output format.

Verify it's working:

```bash  
aws sts get-caller-identity  
```

---

### 3. Install Dependencies

```bash  
pip3 install awsiotsdk  
```

---

### 4. Deploy Greengrass Component

Use AWS Console or CLI to:

- Upload the updated `main.py` and `process_emission.py` to your S3 bucket.
- Register a new Greengrass component (`com.example.EmissionProcessor`).
- Use the following recipe to deploy:

```json
{
  "RecipeFormatVersion": "2020-01-25",
  "ComponentName": "com.example.EmissionProcessor",
  "ComponentVersion": "1.0.1",
  "ComponentDescription": "Component that processes vehicle emission data",
  "ComponentPublisher": "Tamim",
  "ComponentDependencies": {
    "aws.greengrass.TokenExchangeService": {
      "VersionRequirement": ">=2.0.0",
      "DependencyType": "HARD"
    }
  },
  "ComponentConfiguration": {
    "DefaultConfiguration": {
      "accessControl": {
        "aws.greengrass.ipc.mqttproxy": {
          "com.example.EmissionProcessor:mqttproxy:1": {
            "policyDescription": "Allows access to subscribe and publish to MQTT topics",
            "operations": [
              "aws.greengrass#SubscribeToIoTCore",
              "aws.greengrass#PublishToIoTCore"
            ],
            "resources": [
              "vehicle/+/emission",
              "vehicle/+/result"
            ]
          }
        }
      }
    }
  },
  "Manifests": [
    {
      "Platform": {
        "os": "linux"
      },
      "Lifecycle": {
        "Install": "pip3 install awsiotsdk",
        "Run": "python3 {artifacts:path}/main.py"
      },
      "Artifacts": [
        {
          "Uri": "s3://tamim-greengrass-artifacts/artifacts/main.py",
          "Unarchive": "NONE"
        },
        {
          "Uri": "s3://tamim-greengrass-artifacts/artifacts/process_emission.py",
          "Unarchive": "NONE"
        }
      ]
    }
  ]
}
```

---

### 5. Run the Emulator

From KyoSook's repo:

```bash  
cd lab4_cloud/1_build_cloud/3_emulator  
python3 emulator_client.py  
```

When prompted, press `s` to send data and simulate vehicle emissions.

---

### 6. View Logs (On Raspberry Pi or Device)

To verify that your component is running and processing data:

```bash  
sudo tail -f /greengrass/v2/logs/com.example.EmissionProcessor.log  
```

This shows real time processing of published messages like CO₂ values and other metrics.

---

## Policies and Permissions

These were critical to allow Greengrass components to interact with AWS IoT Core:

```text
- SubscribeToIoTCore: vehicle/+/emission
- PublishToIoTCore: vehicle/+/result
```

Configured in the `accessControl` section of the component recipe. Make sure your core device’s token exchange role has permission to access S3 and IoT Core.

---

## Demo Video

We are recording short clips of each step and will merge them into a full 10-minute overview. Current recordings:

- ✅ Setup Greengrass and component deployment
- ✅ Emulator publishing data and Processor receiving logs
- ⏳ Firehose → Glue → Athena → SageMaker (in progress)

Final video will be uploaded soon.

---

## KyoSook's Configuration Notes

Ensure you:

- Clone `lab4_cloud`
- Update your Greengrass device name and credentials
- Deploy `vehicle_sensor` and `vehicle_emulator` components as needed

Refer to her [repo](https://github.com/alla0810/lab4_cloud) for additional setup instructions and documentation.

---

## Troubleshooting

- **Missing logs**: Ensure component is deployed and device is online.
- **MQTT not received**: Check accessControl and IoT policy for permissions.
- **Emulator doesn't connect**: Verify region and IoT endpoint in config.

---

## Authors

- **Mohammad Tamim** – Component Development, Emulator Integration



