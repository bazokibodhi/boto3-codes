# This boto3 program lists out the ec2 instances in the account
# Author : Bodhisatwya Banerjee

import boto3
client = boto3.client('ec2')

ec2_response = client.describe_instances()

# print(ec2_response['Reservations'])

for i in ec2_response['Reservations']:
	# print(i['Instances'])
	for j in i['Instances']:
		print(j['InstanceId'], j['InstanceType'], j['Monitoring'], j['PrivateIpAddress'])
