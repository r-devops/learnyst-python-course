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

    return(response["GroupId"])

def create_ec2_instance(sg_id):
    instance = client.run_instances(
        MaxCount = 1,
        MinCount = 1,
        ImageId='ami-09c813fb71547fc4f',
        InstanceType='t3.micro',
        SecurityGroupIds=[
            'string',
        ],
        SecurityGroups=[
            sg_id,
        ],
    )

if __name__ == '__main__':
    sg_id = create_security_group()
    print(sg_id)
    #create_ec2_instance(sg_id)
