import boto3

AWS_ACCOUNT_ID = '058264177579'
CORE_DEVICE_THING_NAME = 'core_device'  # core device's thing name

iot = boto3.client('iot', region_name='us-east-1')

def detach_and_delete_certificate(cert_id):
    cert_arn = f'arn:aws:iot:us-east-1:{AWS_ACCOUNT_ID}:cert/{cert_id}'
    
    # Detach from policies
    policies = iot.list_principal_policies(principal=cert_arn)['policies']
    for policy in policies:
        print(f" Detaching policy {policy['policyName']} from {cert_id}")
        iot.detach_policy(policyName=policy['policyName'], target=cert_arn)

    # Detach from things
    principals = iot.list_principal_things(principal=cert_arn)['things']
    for thing in principals:
        print(f" Detaching {cert_id} from thing {thing}")
        iot.detach_thing_principal(thingName=thing, principal=cert_arn)

    # Disable and delete certificate
    print(f" Disabling cert {cert_id}")
    iot.update_certificate(certificateId=cert_id, newStatus='INACTIVE')
    print(f" Deleting cert {cert_id}")
    iot.delete_certificate(certificateId=cert_id, forceDelete=True)

def delete_things_and_certificates():
    # List all things
    things = iot.list_things()['things']
    
    for thing in things:
        thing_name = thing['thingName']
        
        # Skip core device
        if thing_name == CORE_DEVICE_THING_NAME:
            print(f"Skipping core device: {thing_name}")
            continue

        print(f"Processing thing: {thing_name}")
        
        # List all certificates attached to this thing
        principals = iot.list_thing_principals(thingName=thing_name)['principals']
        
        for principal in principals:
            cert_arn = principal
            cert_id = cert_arn.split('/')[-1]  # Extract certificate ID from ARN
            print(f" Detaching certificate {cert_id} from thing {thing_name}")
            iot.detach_thing_principal(thingName=thing_name, principal=cert_arn)
            # Delete the certificate
            print(f" Deleting certificate {cert_id}")
            detach_and_delete_certificate(cert_id)
        
        # Delete the thing after handling its certificates
        print(f"Deleting thing: {thing_name}")
        iot.delete_thing(thingName=thing_name)

def main():
    print("Starting AWS IoT cleanup for things and certificates (except core device)...")
    delete_things_and_certificates()
    print("Cleanup complete.")

if __name__ == "__main__":
    main()