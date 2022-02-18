import boto3
from os import environ
environ['AWS_DEFAULT_REGION'] = 'us-west-2'
environ['AWS_ACCESS_KEY_ID'] = 'us-west-2'
environ['AWS_SECRET_ACCESS_KEY'] = 'us-west-2'
sqs = boto3.resource('sqs', region_name='us-west-2')
db = boto3.client('dynamodb',endpoint_url='http://localhost:8000')
# Get the service resource
db = boto3.resource('dynamodb',endpoint_url='http://localhost:8000')

table = db.create_table(
        TableName='Devices',
        KeySchema=[
            {
                'AttributeName': 'device_id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'datacount',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'device_id',
                # AttributeType defines the data type. 'S' is string type and 'N' is number type
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'datacount',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            # ReadCapacityUnits set to 10 strongly consistent reads per second
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10  # WriteCapacityUnits set to 10 writes per second
        }
    )

