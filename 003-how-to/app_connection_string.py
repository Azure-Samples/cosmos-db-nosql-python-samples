"""Sample showing how to connect with connection string."""
import json
import os
import sys
import uuid

from azure.core.exceptions import AzureError
from azure.cosmos import CosmosClient, PartitionKey

DATABASE_ID = "cosmicworks"
CONTAINER_ID = "products"
# <connection_string>
CONN_STR = os.environ["COSMOS_CONNECTION_STRING"]

client = CosmosClient.from_connection_string(conn_str=CONN_STR)
# </connection_string>


def main():
    """How to CosmosDB and NoSQL samples."""
    try:
        # Create database and partition key.
        database = client.create_database_if_not_exists(id=DATABASE_ID)

        # Create a container.
        partition_key_path = PartitionKey(path="/categoryId")
        container = database.create_container_if_not_exists(
            id=CONTAINER_ID, partition_key=partition_key_path,
            offer_throughput=400
        )

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
            query=sql_stmt, parameters=params,
            enable_cross_partition_query=False
        )

        for item in items:
            print(json.dumps(item, indent=True))

    except AzureError as err:
        sys.exit("Error:" + str(err))


if __name__ == "__main__":
    main()
