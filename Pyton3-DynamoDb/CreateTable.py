import boto3
from os import environ


def create_table() : 
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    table = dynamodb.create_table (
        TableName = 'Employees',
        KeySchema = [
            {
                'AttributeName': 'Name',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'Email',
                'KeyType': 'RANGE'
            }
            ],
            AttributeDefinitions = [
                {
                    'AttributeName': 'Name',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName':'Email',
                    'AttributeType': 'S'
                }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits':1,
                    'WriteCapacityUnits':1
                }
            
        )
    print(table)
    return table


if __name__ == '__main__':
    environ['AWS_DEFAULT_REGION'] = 'us-west-2'
    environ['AWS_ACCESS_KEY_ID'] = 'dummy'
    environ['AWS_SECRET_ACCESS_KEY'] = 'dummy'
    device_table = create_table()
    # Print tablle status
    print("Status:", device_table.table_status)
    
  