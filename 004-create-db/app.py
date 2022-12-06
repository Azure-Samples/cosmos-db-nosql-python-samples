"""Sample showing how to connect with endpoint and key."""
import os

from azure.cosmos import CosmosClient
from azure.cosmos.exceptions import CosmosResourceExistsError

DATABASE_ID = "cosmicworks-1"
CONTAINER_ID = "products"
ENDPOINT = os.environ["COSMOS_ENDPOINT"]
KEY = os.environ["COSMOS_KEY"]

client = CosmosClient(url=ENDPOINT, credential=KEY)


def main():
    """How to CosmosDB and NoSQL samples."""
    # <create_database>
    try:
        database = client.create_database(id=DATABASE_ID)
        print(f"Database created: {database.id}")

    except CosmosResourceExistsError:
        print("Database already exists.")
    # </create_database>


if __name__ == "__main__":
    main()
