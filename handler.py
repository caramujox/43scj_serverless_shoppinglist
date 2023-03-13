import json, boto3, random, uuid
from boto3.dynamodb.conditions import Key
from datetime import datetime
from sqsHandler import SqsHandler

#dao = BaseDAO('shopping-list')

def handler(event, context):

  #Setup de variaveis para acesso
    sqs = SqsHandler('https://sqs.us-east-1.amazonaws.com/703846776328/trab-final-serverless')
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table('shopping-list')
    
    print(json.dumps(event))
    
    #Verifica as mensagens na fila, e insere na tabela
    for i in range(100):
        msgs = sqs.getMessage(10)
        print(json.dumps(msgs))
        
        if('Messages' not in msgs):
            break
        if(len(msgs['Messages'])== 0):
            break
        
        for message in msgs['Messages']:
            json.dumps(message['Body'])
            table.put_item(Item= {'item_id': str(uuid.uuid4()), 'name': message['Body']})
            #dao.put_item({'item_id': str(uuid.uuid4()), 'name': message['Body']})
        