import json
import os

from requests import HTTPError
from http import HTTPStatus
from functools import wraps
import boto3 #libraire qui permet de gérer aws avec python
import uuid

#from wrapper import exception_handler

def handler(event, context):
    print('received event:')
    print(event)

# Vérifie si la méthode HTTP est 'POST'
    if event.get('httpMethod') != 'POST':
        # Si ce n'est pas une requête POST, lève une exception
        raise ValueError(f"Méthode HTTP invalide: {event.get('httpMethod')}. Seules les requêtes POST sont autorisées.")
    


    user_table_name = os.environ.get('STORAGE_USERS_NAME')
    if not user_table_name:
        raise ValueError("Nom de la table DynamoDB non défini dans les variables d'environnement.")

    dynamodb = boto3.resource('dynamodb', region_name="eu-west-1")
    table = dynamodb.Table(user_table_name)

     # Parse le corps de la requête JSON en dictionnaire
    try:
        body = json.loads(event['body'])  # Convertit la chaîne JSON en dictionnaire
    except json.JSONDecodeError:
        raise ValueError("Le corps de la requête n'est pas un JSON valide.")
    
    email = body.get('email')  # Utilise maintenant le dictionnaire

    if not email:
        raise ValueError('Email missing')

    # email et GSI emails
    print("Recherche de l'utilisateur dans DynamoDB...")
    res = table.query(
        IndexName='emails',  # Nom du GSI pour les emails
        KeyConditionExpression=boto3.dynamodb.conditions.Key('email').eq(email)
    )
    print(f"Résultat de la requête: {res}")


    user_id = None
    if not res['Items']:
        user_id = str(uuid.uuid4)
        print(f"Aucun utilisateur associé à l'email {email}. Création d'un nouvel utilisateur avec l'ID: {user_id}")

        table.put_item(Item={
            'id': user_id,
            'email': email
        })
    else:
        user_id = res['Items'][0].get('id')
        print(f"Utilisateur trouvé avec l'ID: {user_id}")

    return user_id