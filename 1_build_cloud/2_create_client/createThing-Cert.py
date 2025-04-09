################################################### Connecting to AWS
import boto3
import os
import shutil
import json
################################################### Create random name for things
import random
import string
################################################### Parameters for Thing
thingArn = ''
thingId = ''
defaultPolicyName1 = 'GreengrassV2IoTThingPolicy'
defaultPolicyName2 = 'GreengrassTESCertificatePolicyGreengrassCoreTokenExchangeRoleAlias'
defaultThingGroupName = 'MyGreengrassCoreGroup'
defaultThingGroupArn = 'arn:aws:iot:us-east-1:058264177579:thinggroup/MyGreengrassCoreGroup'
###################################################

thingClient = boto3.client('iot')

core_cert_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "certertificates")

#Path to your certificates, modify this
core_device_certificate_path = os.path.join(core_cert_dir, "thingCert.crt")
core_device_key_path = os.path.join(core_cert_dir, "privKey.key")
core_device_root_ca_path = os.path.join(core_cert_dir, "rootCA.pem")

def copy_certificates():
    # Path to the source and destination directories
    source_cert_dir = "/greengrass/v2/"
    dest_cert_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "certertificates")

    # List of the required certificate files
    cert_files = ["privKey.key", "thingCert.crt", "rootCA.pem"]

    # Ensure the destination directory exists
    if not os.path.exists(dest_cert_dir):
        os.mkdir(dest_cert_dir)

    # Copy certificate files from /greengrass/v2/ to cert directory
    for cert_file in cert_files:
        source_file_path = os.path.join(source_cert_dir, cert_file)
        dest_file_path = os.path.join(dest_cert_dir, cert_file)

        if os.path.exists(source_file_path):
            try:
                # Check if the file is readable
                if not os.access(source_file_path, os.R_OK):
                    print(f"Error: {cert_file} is not readable.")
                    continue

                # Attempt to copy the file
                shutil.copy(source_file_path, dest_file_path)
                print(f"Successfully copied {cert_file} to {dest_cert_dir}")

            except PermissionError:
                print(f"PermissionError: Unable to access {cert_file} from {source_cert_dir}")
                print("Attempting to run with elevated privileges (sudo)...")

                # Try running with sudo if needed (e.g., using subprocess)
                import subprocess
                subprocess.run(["sudo", "python3", __file__])
                break

        else:
            print(f"Error: {cert_file} does not exist in {source_cert_dir}")


def createThing(thingName):
  global thingClient
  thingResponse = thingClient.create_thing(
      thingName = thingName
  )
  data = json.loads(json.dumps(thingResponse, sort_keys=False, indent=4))
  thingArn = data.get('thingArn','')
  thingId = data.get('thingId', '')

  createCertificate(thingName)

def createCertificate(thingName):
	global thingClient

	certDir = './certificates'
	certFile = os.path.join(certDir, f'{thingName}_cert.pem')

	if os.path.exists(certFile):
		print(f"Certificate for {thingName} already exists.  Skipping certificate creation")
		return
	
	if not os.path.exists(certDir):
		os.mkdir(certDir)	

	certResponse = thingClient.create_keys_and_certificate(
			setAsActive = True
	)
	
	data = json.loads(json.dumps(certResponse, sort_keys=False, indent=4))
	certificateArn = data.get('certificateArn', '')
	PublicKey = data.get('keyPair', {}).get('PublicKey', '')
	PrivateKey = data.get('keyPair', {}).get('PrivateKey', '')
	certificatePem = data.get('certificatePem', '')
	certificateId = data.get('certificateId', '')

	if not os.path.exists(certDir):
		os.mkdir(certDir)
						
	with open(os.path.join(certDir, f'{thingName}_public.key'), 'w') as outfile:
			outfile.write(PublicKey)
	with open(os.path.join(certDir, f'{thingName}_private.key'), 'w') as outfile:
			outfile.write(PrivateKey)
	with open(os.path.join(certDir, f'{thingName}_cert.pem'), 'w') as outfile:
			outfile.write(certificatePem)

	response = thingClient.attach_policy(
			policyName = defaultPolicyName1,
			target = certificateArn
	)
	response = thingClient.attach_policy(
			policyName = defaultPolicyName2,
			target = certificateArn
	)

	response = thingClient.attach_thing_principal(
			thingName = thingName,
			principal = certificateArn
	)
	response = thingClient.add_thing_to_thing_group(
		    thingGroupName=defaultThingGroupName,
			thingGroupArn=defaultThingGroupArn,
			thingName=thingName,
			thingArn=thingArn
	)


def main(): 
	certDir = './certificates'
	if os.path.exists(certDir):
		shutil.rmtree(certDir)
	os.mkdir(certDir)	

	copy_certificates()


	for i in range(5):
		thingName = 'vehicle_' + str(i)

		createThing(thingName)

if __name__ == '__main__':
	main()