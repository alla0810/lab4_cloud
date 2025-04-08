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
defaultPolicyName = 'GreengrassV2IoTThingPolicy'
defaultThingGroupName = 'MyGreengrassCoreGroup'
defaultThingGroupArn = 'arn:aws:iot:us-east-1:058264177579:thinggroup/MyGreengrassCoreGroup'
###################################################

thingClient = boto3.client('iot')

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
			policyName = defaultPolicyName,
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


	for i in range(5):
		thingName = 'vehicle_' + str(i)

		createThing(thingName)

if __name__ == '__main__':
	main()