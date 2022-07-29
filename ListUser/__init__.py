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
app_client = GraphClient(credential=client_credential, scopes=['https://graph.microsoft.com/.default'])

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    result = get_users()
    
    headers = { "Content-Type": "application/json"}
    return func.HttpResponse(json.dumps(result), headers=headers)
        

def get_users():
    endpoint = '/users'
    # Only request specific properties
    select = 'displayName,id,mail'
    # Get at most 25 results
    top = 25
    # Sort by display name
    order_by = 'displayName'
    request_url = f'{endpoint}?$select={select}&$top={top}&$orderBy={order_by}'

    users_response = app_client.get(request_url)
    return users_response.json()

    