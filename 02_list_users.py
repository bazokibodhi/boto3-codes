# This is a sample boto3 program which lists out number of IAM users
# Author : Bodhisatwya Banerjee

import boto3
client = boto3.client('iam')

output = client.list_users()

# print(output['Users'])

for new_output in output['Users']:
	print(new_output['UserName'], new_output['UserId'], new_output['Arn'], new_output['CreateDate'])

