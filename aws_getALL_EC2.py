import boto3


def get_instance_name(fid):
    ec2 = boto3.resource('ec2')
    ec2instance = ec2.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    return instancename
    
def get_instance_env(fid):
    ec2 = boto3.resource('ec2')
    ec2instance = ec2.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'ENV':
            instancename = tags["Value"]
    return instancename

def get_instance_purpose(fid):
    ec2 = boto3.resource('ec2')
    ec2instance = ec2.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'Purpose':
            instancename = tags["Value"]
    return instancename

def get_instance_pack(fid):
    ec2 = boto3.resource('ec2')
    ec2instance = ec2.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'Pack':
            instancename = tags["Value"]
    return instancename

ec2 = boto3.resource(service_name='ec2',
                     region_name='ap-southeast-1234',
                     aws_access_key_id='key',
                     aws_secret_access_key='key')

for i in ec2.instances.all():
    prod="prod"
    fuck = get_instance_env(i.instance_id)
    if fuck == prod :
        print(i.private_ip_address,i.public_ip_address,i.instance_id,get_instance_name(i.instance_id),get_instance_env(i.instance_id),get_instance_purpose(i.instance_id), get_instance_pack(i.instance_id) )
    else:
        pass
        

