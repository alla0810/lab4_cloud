import boto3

AWS_ACCOUNT_ID = '058264177579'

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

def delete_all_things():
    things = iot.list_things()['things']
    for thing in things:
        thing_name = thing['thingName']
        print(f"Deleting thing: {thing_name}")
        principals = iot.list_thing_principals(thingName=thing_name)['principals']
        for principal in principals:
            iot.detach_thing_principal(thingName=thing_name, principal=principal)
        iot.delete_thing(thingName=thing_name)

def delete_all_certificates():
    certs = iot.list_certificates()['certificates']
    for cert in certs:
        cert_id = cert['certificateId']
        print(f"Handling certificate: {cert_id}")
        detach_and_delete_certificate(cert_id)

def delete_all_policies():
    policies = iot.list_policies()['policies']
    for policy in policies:
        policy_name = policy['policyName']
        print(f"Deleting policy: {policy_name}")
        iot.delete_policy(policyName=policy_name)

def delete_all_thing_groups():
    groups = iot.list_thing_groups()['thingGroups']
    for group in groups:
        name = group['groupName']
        print(f"Deleting thing group: {name}")
        iot.delete_thing_group(thingGroupName=name)

def main():
    print("🧹 Starting AWS IoT cleanup...")
    delete_all_things()
    delete_all_certificates()
    delete_all_policies()
    delete_all_thing_groups()
    print("✅ Cleanup complete.")

if __name__ == "__main__":
    main()
