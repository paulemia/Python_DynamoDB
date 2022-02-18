import boto3
from os import environ
####  setting Environment 
environ['AWS_DEFAULT_REGION'] = 'us-west-2'
environ['AWS_ACCESS_KEY_ID'] = 'dummy'
environ['AWS_SECRET_ACCESS_KEY'] = 'dummy'

import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Employees')

with table.batch_writer() as batch:
    
    batch.put_item(Item={"Name": "Luzze John", "Email": "john@handson.cloud",
        "Department": "IT", "Section": { "QA": "QA-1", "Reporting Line": "L1" } })
    batch.put_item(Item={"Name": "Lugugo Joshua", "Email": "joshua@handson.cloud",
        "Department": "IT", "Section": { "Development": "SD-1", "Reporting Line": "L1" } })
    batch.put_item(Item={"Name": "Robert Nsamba", "Email": "robert@handson.cloud",
        "Department": "IT", "Section": { "PM": "PM-1", "Reporting Line": "L1" } })
print(batch)