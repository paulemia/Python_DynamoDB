import boto3
from os import environ
import json
import os

environ['AWS_DEFAULT_REGION'] = 'us-west-2'
environ['AWS_ACCESS_KEY_ID'] = 'dummy'
environ['AWS_SECRET_ACCESS_KEY'] = 'dummy'
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = dynamodb.Table('RcmData')


FilePath = r'C:\Users\DP966UZ\OneDrive - EY\Documents\wawa\data\RCM_data_load_jSampl0808.json'
with open(FilePath, encoding='utf-8-sig') as file:
        dataReader = json.load(file)
        with table.batch_writer() as batch:

        # Loop through the JSON objects
        
          
            for item in dataReader['datarows']:
                batch.put_item(Item=item) 
                print(table.item_count)
              