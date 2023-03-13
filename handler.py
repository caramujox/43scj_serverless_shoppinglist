import json, boto3, random, uuid
from boto3.dynamodb.conditions import Key
from datetime import datetime
from sqsHandler import SqsHandler

#dao = BaseDAO('shopping-list')

def handler(event, context):
    #env = Variables()
    sqs = SqsHandler('https://sqs.us-east-1.amazonaws.com/019395563129/trab-final-serverless')
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table('shopping-list')
    
    print(json.dumps(event))
    
    for record in event['Records']:
        msgs = sqs.getMessage(10)
        print("msgs:::::" + json.dumps(msgs))
        print("PRINTANDO STATUS: " + json.dumps(msgs))
        
        print("Item " + record["body"] + " incluido com sucesso!")
        table.put_item(Item= {'item_id': str(uuid.uuid4()), 'name': record['body']})
            #dao.put_item({'item_id': str(uuid.uuid4()), 'name': message['Body']})
        