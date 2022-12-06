"""Sample showing how to connect with AAD service principal."""
import json
import os
import sys
import uuid

from azure.core.exceptions import AzureError
from azure.cosmos import CosmosClient

# <credential>
from azure.identity import ClientSecretCredential

ENDPOINT = os.environ["COSMOS_ENDPOINT"]
TENANT_ID = os.environ["TENANT_ID"]
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]

credential = ClientSecretCredential(
    tenant_id=TENANT_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)

client = CosmosClient(ENDPOINT, credential)
# </credential>

DATABASE_ID = "cosmicworks"
CONTAINER_ID = "products"


def main():
    """How to CosmosDB and NoSQL samples."""
    try:
        # Get database.
        database = client.get_database_client(DATABASE_ID)

        # Get container.
        container = database.get_container_client(CONTAINER_ID)
        print("Container info: " + str(container.read()))

        # Create a new item.
        new_guid = str(uuid.uuid4())
        new_item = {
            "id": new_guid,
            "categoryId": "61dba35b-4f02-45c5-b648-c6badc0cbd79",
            "categoryName": "gear-surf-surfboards",
            "name": "Yamba Surfboard",
            "quantity": 12,
            "sale": False,
        }
        container.create_item(new_item)

        # Query items.
        sql_stmt = "SELECT * FROM products p WHERE p.categoryId = @categoryId"
        category_id = "61dba35b-4f02-45c5-b648-c6badc0cbd79"
        params = [dict(name="@categoryId", value=category_id)]

        items = container.query_items(
            query=sql_stmt, parameters=params, enable_cross_partition_query=False
        )

        for item in items:
            print(json.dumps(item, indent=True))

    except AzureError as err:
        sys.exit("Error:" + str(err))


if __name__ == "__main__":
    main()
