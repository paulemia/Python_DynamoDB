import boto3
from boto3.dynamodb.conditions import Key, Attr
from os import environ
import json 

environ['AWS_DEFAULT_REGION'] = 'us-west-2'
environ['AWS_ACCESS_KEY_ID'] = 'dummy'
environ['AWS_SECRET_ACCESS_KEY'] = 'dummy'

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Employees')

##response = table.scan(FilterExpression=Attr('Name').contains('Art'))
response = table.scan(FilterExpression=Attr('Name').begins_with('Art'))

print("The query returned the following items:")
for item in response['Items']:
    print(item)