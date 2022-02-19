import boto3
from os import environ

environ['AWS_DEFAULT_REGION'] = 'us-west-2'
environ['AWS_ACCESS_KEY_ID'] = 'dummy'
environ['AWS_SECRET_ACCESS_KEY'] = 'dummy'

 

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Employees')
for i in range( 10)  : 
    name =  'Artur Bakh' + str(i)
    email = 'fakeemail@yahoo.com'
    response = table.put_item(
    Item = { 'Name': name   ,
             'Email':  email 
        }
    )
print(response)