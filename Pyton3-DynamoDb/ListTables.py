import boto3
from os import environ

environ['AWS_DEFAULT_REGION'] = 'us-west-2'
environ['AWS_ACCESS_KEY_ID'] = 'dummy'
environ['AWS_SECRET_ACCESS_KEY'] = 'dummy'

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

print(list(dynamodb.tables.all()))