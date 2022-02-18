import boto3
from os import environ

environ['AWS_DEFAULT_REGION'] = 'us-west-2'
environ['AWS_ACCESS_KEY_ID'] = 'dummy'
environ['AWS_SECRET_ACCESS_KEY'] = 'dummy'

import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Employees')
for i in range( 10)  : 
    response = table.put_item(
    Item = { 'Name': 'Artur Bakh'  + str(i) ,
             'Email': 'artur_olga@yahoo.com'
        }
    )
print(response)