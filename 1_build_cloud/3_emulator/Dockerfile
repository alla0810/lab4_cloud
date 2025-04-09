FROM python:3.11

WORKDIR /home

RUN apt-get update && apt-get install -y vim && rm -rf /var/lib/apt/lists/*

RUN pip install AWSIoTPythonSDK pandas numpy awscrt awsiot boto3 awsiotsdk

COPY ./basic_discovery.py /home/basic_discovery.py
COPY ./utils /home/utils
COPY ./emulator_client.py /home/emulator_client.py
COPY ./data /home/data

COPY ./certificates /home/certificates

ENV DEVICE_ID=vehicle_0

CMD ["bash"]
