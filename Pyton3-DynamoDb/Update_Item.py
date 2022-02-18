import boto3
from os import environ
 

environ['AWS_DEFAULT_REGION'] = 'us-west-2'
environ['AWS_ACCESS_KEY_ID'] = 'dummy'
environ['AWS_SECRET_ACCESS_KEY'] = 'dummy'

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Employees')


response = table.update_item(
    Key={'Name': 'Robert Nsamba', 'Email': 'robert@handson.cloud'},
    ExpressionAttributeNames={
        "#section": "Section",
        "#reportingline": "Reporting Line"
       
        },
        ExpressionAttributeValues={
            ':id': 'New Reporting Line 222' 
           
        },
        UpdateExpression="SET #section.#reportingline = :id ",
    )
print(response)


response = table.update_item(
    Key={'Name': 'Artur Bakh4', 'Email': 'artur_olga@yahoo.com'},
    ExpressionAttributeNames={
        "#age": "Age" ,
        "#department":"Department",
        "#boss": "Boss"
       
        },
        ExpressionAttributeValues={
            ':age': 54 , 
            ":dep":"IT",
             ":boss": "gandon shtopannii"
           
        },
        UpdateExpression="SET #age = :age ,#department = :dep , #boss =:boss" , 
    )
print(response)

