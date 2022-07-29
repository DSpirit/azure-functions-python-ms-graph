import logging
import os
import json
import azure.functions as func
from azure.identity import ClientSecretCredential
from azure.graphrbac import GraphRbacManagementClient	
from msgraph.core import GraphClient

# Define
client_id = os.environ['CLIENT_ID']
tenant_id = os.environ['TENANT_ID']
client_secret = os.environ['CLIENT_SECRET']

# Authenticate
client_credential = ClientSecretCredential(tenant_id, client_id, client_secret)

# Instantiate
app_client = GraphClient(credential=client_credential, scopes=['https://graph.windows.net/.default'])

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    user = req.get_json()
    result = create_user(user)
    
    headers = { "Content-Type": "application/json"}
    return func.HttpResponse(json.dumps(result), headers=headers)
        

def create_user(user):
    endpoint = '/users'
    
    request_url = f'{endpoint}'
    headers = { "Content-Type": "application/json"}

    users_response = app_client.post(request_url, json.dumps(user), headers=headers)
    return users_response.json()

    