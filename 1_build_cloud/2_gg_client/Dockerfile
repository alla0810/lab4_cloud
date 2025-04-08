FROM python:3.11

WORKDIR /home

RUN pip install AWSIoTPythonSDK pandas numpy awscrt awsiot boto3

COPY ./basic_discovery.py /home/basic_discovery.py
COPY ./utils /home/utils

COPY ./certificates /home/certificates

ENV DEVICE_ID vehicle_0

CMD ["bash"]
