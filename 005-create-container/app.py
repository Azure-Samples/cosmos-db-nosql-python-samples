"""Sample showing how to connect with endpoint and key."""
import os

from azure.cosmos import CosmosClient, PartitionKey
from azure.cosmos.exceptions import (CosmosHttpResponseError,
                                     CosmosResourceExistsError)

DATABASE_ID = "cosmicworks-1"
CONTAINER_ID = "products"
ENDPOINT = os.environ["COSMOS_ENDPOINT"]
KEY = os.environ["COSMOS_KEY"]

client = CosmosClient(url=ENDPOINT, credential=KEY)


def main():
    """How to CosmosDB and NoSQL samples."""
    try:
        database = client.create_database_if_not_exists(id=DATABASE_ID)

        # <create_container>
        try:
            partition_key_path = PartitionKey(path="/categoryId")
            container = database.create_container(
                id=CONTAINER_ID, partition_key=partition_key_path,
                offer_throughput=400
            )
            print(f"Container created: {container.id}")

        except CosmosResourceExistsError:
            print("Container already exists.")
        # </create_container>

    except CosmosHttpResponseError:
        print("Request to the Azure Cosmos database service failed.")


if __name__ == "__main__":
    main()
