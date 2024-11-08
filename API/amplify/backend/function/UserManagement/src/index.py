import json
import os

from requests import HTTPError
from http import HTTPStatus
from functools import wraps
import boto3 #libraire qui permet de gérer aws avec python

from wrapper import exception_handler

#amplify add storage = créer une bd
@exception_handler
def handler(event, context):

# Vérifie si la méthode HTTP est 'GET'
    if event.get('httpMethod') != 'GET':
        # Si ce n'est pas une requête GET, lève une exception
        raise ValueError(f"Méthode HTTP invalide: {event.get('httpMethod')}. Seules les requêtes GET sont autorisées.")
    
    
    user_table_name = os.environ.get('STORAGE_USERS_NAME')
    dynamodb = boto3.resource('dynamodb', region_name="eu-west-1")
    table = dynamodb.Table(user_table_name)
    
    user_id = event['headers']['x-api-key']
    res = table.get_item(
        Key={'id': user_id}
    )

    data = res.get('Item')
    if not data:
        raise ValueError('User missing')

    


    return data['email']
  
#   return {
#       'statusCode': 200,
#       'headers': {
#           'Access-Control-Allow-Headers': '*',
#           'Access-Control-Allow-Origin': '*',
#           'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
#       },
#       'body': json.dumps('Hello from your new Amplify Python lambda!')
#   }

