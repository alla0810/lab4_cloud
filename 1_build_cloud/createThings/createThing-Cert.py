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
defaultPolicyName = 'policy1'
###################################################

def createThing(thingName):
  global thingClient
  thingResponse = thingClient.create_thing(
      thingName = thingName
  )
  data = json.loads(json.dumps(thingResponse, sort_keys=False, indent=4))
  for element in data: 
    if element == 'thingArn':
        thingArn = data['thingArn']
    elif element == 'thingId':
        thingId = data['thingId']
    createCertificate(thingName)

def createCertificate(thingName):
	global thingClient
	certResponse = thingClient.create_keys_and_certificate(
			setAsActive = True
	)
	data = json.loads(json.dumps(certResponse, sort_keys=False, indent=4))
	for element in data: 
			if element == 'certificateArn':
					certificateArn = data['certificateArn']
			elif element == 'keyPair':
					PublicKey = data['keyPair']['PublicKey']
					PrivateKey = data['keyPair']['PrivateKey']
			elif element == 'certificatePem':
					certificatePem = data['certificatePem']
			elif element == 'certificateId':
					certificateId = data['certificateId']
							
	with open(os.path.join('certificates', '') + thingName + '_public.key', 'w') as outfile:
			outfile.write(PublicKey)
	with open(os.path.join('certificates', '') + thingName + '_private.key', 'w') as outfile:
			outfile.write(PrivateKey)
	with open(os.path.join('certificates', '') + thingName + '_cert.pem', 'w') as outfile:
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
		    thingGroupName='ThingGroup1',
			thingGroupArn='arn:aws:iot:us-east-1:058264177579:thinggroup/ThingGroup1',
			thingName=thingName,
			thingArn=thingArn
	)


certDir = "./certificates"
if os.path.exists(certDir):
	shutil.rmtree(certDir)
os.mkdir(certDir)

thingClient = boto3.client('iot')

def main(): 
	for i in range(5):
		thingName = 'vehicle_' + str(i)

		createThing(thingName)

if __name__ == '__main__':
	main()