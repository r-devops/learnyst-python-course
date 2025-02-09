# Create a EC2 Instance with Own Security Group
import boto3

client = boto3.client('ec2', region_name='us-east-1')

def create_security_group():
    response = client.create_security_group(
        Description='boto3_example',
        GroupName='boto3_example'
    )

if __name__ == '__main__':
    create_security_group()