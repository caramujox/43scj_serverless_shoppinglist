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
    
    for i in range(100):
        msgs = sqs.getMessage(10)
        for record in event['Records']:
            payload = record['body']
            #print("msgs:::::" + msgs['Messages'])
            print("PRINTANDO PAYLOAD: " + json.dumps(payload))
            table.put_item(Item= {'item_id': str(uuid.uuid4()),'datetime': str(datetime.now()),  'name': record['body']})
            #print("Item " + record["body"] + " incluido com sucesso!")