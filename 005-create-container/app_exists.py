"""Sample showing how to connect with endpoint and key."""
import os

from azure.cosmos import CosmosClient, PartitionKey
from azure.cosmos.exceptions import CosmosHttpResponseError

DATABASE_ID = "cosmicworks-3"
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
            container = database.create_container_if_not_exists(
                id=CONTAINER_ID,
                partition_key=partition_key_path,
                offer_throughput=400,
            )
            print(f"Container created or returned: {container.id}")

        except CosmosHttpResponseError:
            print("Request to the Azure Cosmos database service failed.")
        # </create_container>

        try:
            # <parse_response>
            partition_key_path = PartitionKey(path="/categoryId")
            container = database.create_container_if_not_exists(
                id=CONTAINER_ID,
                partition_key=partition_key_path,
                offer_throughput=400,
            )
            for doc in container.read_all_items(max_item_count=10):
                print(f'Doc id: {doc["id"]}')
            # </parse_response>

        except CosmosHttpResponseError:
            print("Request to the Azure Cosmos database service failed.")

    except CosmosHttpResponseError:
        print("Request to the Azure Cosmos database service failed.")


if __name__ == "__main__":
    main()
