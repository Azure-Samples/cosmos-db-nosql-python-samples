"""Sample showing how to connect with endpoint and key."""
import os

from azure.cosmos import CosmosClient
from azure.cosmos.exceptions import CosmosHttpResponseError

DATABASE_ID = "cosmicworks-1"
CONTAINER_ID = "products"
ENDPOINT = os.environ["COSMOS_ENDPOINT"]
KEY = os.environ["COSMOS_KEY"]

client = CosmosClient(url=ENDPOINT, credential=KEY)


def main():
    """How to CosmosDB and NoSQL samples."""
    # <create_database>
    try:
        database = client.create_database_if_not_exists(id=DATABASE_ID)
        print(f"Database created or returned: {database.id}")

    except CosmosHttpResponseError:
        print("Request to the Azure Cosmos database service failed.")
    # </create_database>

    try:
        # <parse_response>
        database = client.create_database_if_not_exists(id=DATABASE_ID)
        for container in database.list_containers():
            print(f'Container name: {container["id"]}')

        # </parse_response>

    except CosmosHttpResponseError:
        print("Request to the Azure Cosmos database service failed.")


if __name__ == "__main__":
    main()
