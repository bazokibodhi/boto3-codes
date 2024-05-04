# This boto3 program lists out the ebs volumes and their respective details
# Author : Bodhisatwya Banerjee
# Version : v2.0
# Date : 2024.05.03

import boto3
client = boto3.client('ec2')

volumes = client.describe_volumes()

# print(volumes['Volumes'])
for new_volumes in volumes['Volumes']:
	print(new_volumes['VolumeId'], new_volumes['SnapshotId'], new_volumes['State'], new_volumes['VolumeType'])
