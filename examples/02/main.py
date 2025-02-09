# Create a EC2 Instance with Own Security Group
import boto3

client = boto3.client('ec2', region_name='us-east-1')

def create_security_group():
    response = client.create_security_group(
        Description='boto3_example',
        GroupName='boto3_example'
    )
    response_for_ingress = client.authorize_security_group_ingress(
        GroupId=response["GroupId"],
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [
                    {
                        'Description': 'Allow SSH',
                        'CidrIp': '0.0.0.0/0',
                    },
                ]
            },
        ],
    )

if __name__ == '__main__':
    create_security_group()