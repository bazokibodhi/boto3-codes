# This sample boto3 program lists out the number of IAM groups
# Author : Bodhisatwya Banerjee
# Version : v1.0
# Date : 02.05.2024

import boto3
client = boto3.client('iam')

group_output = client.list_groups()

# print(group_output['Groups'])

for new_group_output in group_output['Groups']:
	print(new_group_output['GroupName'], new_group_output['GroupId'], new_group_output['CreateDate'])
