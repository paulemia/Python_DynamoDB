import boto3
from os import environ

def create_table() : 
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    table = dynamodb.create_table (
        TableName = 'Employees2',
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




    
def create_table_name(table_name) : 
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    try : 
      client = boto3.client('dynamodb' ,  endpoint_url="http://localhost:8000")  
      resp = client.delete_table (  TableName=table_name , )
      print('Table Deleted delete') 
    except Exception as e:
        print("Error deleting table:")
        print(e) 
    table = dynamodb.create_table (
        TableName = table_name,
        KeySchema = [
            {
                'AttributeName': 'retailItemModifiedId',
                'KeyType': 'HASH'
            }            
            ],
            AttributeDefinitions = [
                {
                    'AttributeName': 'retailItemModifiedId',
                    'AttributeType': 'N'
                }              
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits':1,
                    'WriteCapacityUnits':1
                }
            
        )
    table.wait_until_exists()   
    # Print out some data about the table.
    print(table.item_count)
    return table


if __name__ == '__main__':
    environ['AWS_DEFAULT_REGION'] = 'us-west-2'
    environ['AWS_ACCESS_KEY_ID'] = 'dummy'
    environ['AWS_SECRET_ACCESS_KEY'] = 'dummy'
    device_table= create_table_name("RcmData")
    print("Status:", device_table.table_status)
    
  