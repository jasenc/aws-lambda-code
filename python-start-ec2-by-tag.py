import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):

    filters = [{'Name': 'tag:auto-start', 'Values': ['yes']},
               {'Name': 'instance-state-name', 'Values': ['stopped']}]

    instances = ec2.instances.filter(Filters=filters)
    StoppedInstances = [instance.id for instance in instances]
    print(StoppedInstances)

    if len(StoppedInstances) > 0:
        startingUp = ec2.instances.filter(
            InstanceIds=StoppedInstances).start()
        print(startingUp)
