# Setup (Ubuntu 22 LTS)
- sudo apt install software-properties-common
- sudo add-apt-repository ppa:deadsnakes/ppa
- sudo apt install python3.9
- sudo apt-get install python3.9-dev python3.9-venv
- python3.9 -m venv sandbox
- source sandbox/bin/activate
- func host start

# Configure your local.settings.json
In order to use the functions, you need to correctly configure a local.settings.json file.
Here's an example:
``` json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopment=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "CLIENT_ID": "<your-client-id>",
    "TENANT_ID": "<your-tenant-id>",
    "CLIENT_SECRET": "<your-client-secret>"
  }
}
```

# Test
Install the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) and open the tests.http in Visual Studio Code.
When running the function, you can either list Azure AD users or create new users.

# Links
- https://marketplace.visualstudio.com/items?itemName=humao.rest-client
- https://docs.microsoft.com/en-us/graph/tutorials/python?tabs=aad
- https://dev.to/425show/azure-functions-azure-ad-b2c-and-python-876
- https://docs.microsoft.com/en-us/python/api/overview/azure/microsoft-graph?view=azure-python