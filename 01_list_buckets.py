# This is a sample boto3 program to list out number of buckets in this account
# Author : Bodhisatwya Banerjee

import boto3
client = boto3.client('s3')

output = client.list_buckets()

# print(output['Buckets'])

for list_of_buckets in output['Buckets']:
	print(list_of_buckets['Name'], list_of_buckets['CreationDate'])
