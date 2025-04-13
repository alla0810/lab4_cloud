import boto3
import pandas as pd
import json
import os

# Initialize Firehose client
firehose_client = boto3.client(
    "firehose", region_name="us-east-2"
)  # Replace with your AWS region

# Firehose delivery stream name
delivery_stream_name = "PUT-S3-oKN3O"

# Path to the dataset files
data_path = "../1_build_cloud/3_emulator/data/vehicle{}.csv"


def push_to_firehose(file_index):
    """
    Push data from a specific vehicle CSV file to the Firehose delivery stream.
    """
    file_path = data_path.format(file_index)
    if not os.path.exists(file_path):
        print(f"[ERROR] File {file_path} does not exist.")
        return

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Iterate through each row and send to Firehose
    for _, row in df.iterrows():
        payload = json.dumps(row.to_dict())  # Convert row to JSON
        try:
            response = firehose_client.put_record(
                DeliveryStreamName=delivery_stream_name,
                Record={"Data": payload + "\n"},  # Add newline for S3 compatibility
            )
            print(f"[SUCCESS] Sent record to Firehose: {response}")
        except Exception as e:
            print(f"[ERROR] Failed to send record to Firehose: {e}")


def main():
    # Push data from vehicle0.csv to vehicle4.csv
    for i in range(5):  # Files are named vehicle0.csv to vehicle4.csv
        print(f"Pushing data from vehicle{i}.csv to Firehose...")
        push_to_firehose(i)


if __name__ == "__main__":
    main()
