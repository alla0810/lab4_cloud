import json
import time
import traceback
import sys
import boto3

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
from awsiot.greengrasscoreipc.model import (
    SubscribeToIoTCoreRequest,
    QOS,
    PublishToIoTCoreRequest,
)
from process_emission import process_emission_data

SUBSCRIPTION_TOPIC = "vehicle/+/emission"

firehose_client = boto3.client(
    "firehose", region_name="us-east-2"
)  # Replace with your AWS region

# Firehose delivery stream name
FIREHOSE_STREAM_NAME = "PUT-S3-oKN3O"

# IPC v2 client
ipc_client = GreengrassCoreIPCClientV2()


class StreamHandler:
    def __call__(self, event):
        try:
            topic = event.message.topic_name
            payload_str = event.message.payload.decode("utf-8")
            message = json.loads(payload_str)

            print(f"[RECEIVED] Topic: {topic}, Payload: {payload_str}")

            vehicle_id = topic.split("/")[1]
            result = process_emission_data(message)

            result_topic = f"vehicle/{vehicle_id}/result"
            result_message = json.dumps(result)

            # Publish result
            ipc_client.publish_to_iot_core(
                topic_name=result_topic,
                qos=QOS.AT_LEAST_ONCE,
                payload=bytes(result_message, "utf-8"),
            )

            print(f"[PUBLISHED] Topic: {result_topic}, Payload: {result_message}")

            # Send result to Firehose
            firehose_client.put_record(
                DeliveryStreamName=FIREHOSE_STREAM_NAME,
                Record={
                    "Data": result_message + "\n"
                },  # Firehose expects newline-delimited records
            )
            print(f"[FIREHOSE] Sent data to Firehose stream: {FIREHOSE_STREAM_NAME}")

        except Exception as e:
            print(f"[ERROR] Failed to process message: {e}")
            traceback.print_exc(file=sys.stdout)


def subscribe_to_topic():
    print(f"Subscribing to topic: {SUBSCRIPTION_TOPIC}")
    try:
        request = SubscribeToIoTCoreRequest()
        request.topic_name = SUBSCRIPTION_TOPIC
        request.qos = QOS.AT_LEAST_ONCE

        operation = ipc_client.new_subscribe_to_iot_core(StreamHandler())
        operation.activate(request)
        operation.get_response().result()  # Wait for successful subscription

        print("Subscription successful")
    except Exception as e:
        print(f"[ERROR] Failed to subscribe: {e}")
        traceback.print_exc(file=sys.stdout)


def main():
    try:
        subscribe_to_topic()
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nGracefully shutting down.")
    except Exception as e:
        print(f"[FATAL] {e}")
        traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    main()
