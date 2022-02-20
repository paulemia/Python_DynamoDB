import boto3
from os import environ
import json 

environ['AWS_DEFAULT_REGION'] = 'us-west-2'
environ['AWS_ACCESS_KEY_ID'] = 'dummy'
environ['AWS_SECRET_ACCESS_KEY'] = 'dummy'

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = dynamodb.Table('RcmData')


def iterdict(d):
  for k,v in d.items():        
     if isinstance(v, dict):
         print (f'Parent :Child {k}: {v}  '  )
         iterdict(v)
     else:            
        print (f'key :val {k}: {v}  '  )







'''
for i in range(10)  : 
    response = table.get_item(
    Key = { 'Name': 'Artur Bakh'  + str(i) ,
             'Email': 'artur_olga@yahoo.com'
        }

    )
    print(response['Item']) 
  '''
    ###########################Read it all 






response = table.scan()

#####    Scan all Table data and load to list
dataset = response['Items'] 
 
 
#####   each recors in lisy 
for rec  in dataset : 
    print(rec)
 ##  print(dataset[rec])
    iterdict(rec)      
###map(iterdict,dataset )
''' 
response = table.get_item(
    Key = {  'Name': 'Robert Nsamba'   , 'Email': 'robert@handson.cloud'}  )

print( 'geting single item ' ,  response['Item'] )

print( 'geting single Type' ,  type(response['Item']) )

print( '  Loooping thru   Dictonary '  )

for k, v in response['Item'].items():
    print (f'key :value {k}: {v}  '  )
'''
         


