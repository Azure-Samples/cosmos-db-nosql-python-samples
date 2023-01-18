# <imports>
import os
import json
import asyncio

from azure.cosmos import PartitionKey
from azure.cosmos.aio import CosmosClient

# </imports>

# <environment_variables>
ENDPOINT = os.environ["COSMOS_ENDPOINT"]
KEY = os.environ["COSMOS_KEY"]
# </environment_variables>

# <constants>
DATABASE_NAME = 'cosmicworks'
CONTAINER_NAME = 'products'
# </constants>

# <async_code>
async def manage_cosmos():
    async with CosmosClient(url=ENDPOINT, credential=KEY) as client:
        database = await client.create_database_if_not_exists(id=DATABASE_NAME)
        print("Database", database)
        
        
        partition_key_path = PartitionKey(path="/categoryId")
        
        container = await database.create_container_if_not_exists(
            id=CONTAINER_NAME, partition_key=partition_key_path, offer_throughput=400
        )
        print("Container", container)
        
        new_item = {
          "id": "70b63682-b93a-4c77-aad2-65501347265f",
          "categoryId": "61dba35b-4f02-45c5-b648-c6badc0cbd79",
          "categoryName": "gear-surf-surfboards",
          "name": "Yamba Surfboard",
          "quantity": 12,
          "sale": False,
        }
        
         created_item = await container.create_item(new_item)
        
        existing_item = await container.read_item(
            item="70b63682-b93a-4c77-aad2-65501347265f",
            partition_key="61dba35b-4f02-45c5-b648-c6badc0cbd79",
        )

        QUERY = "SELECT * FROM products p WHERE p.categoryId = @categoryId"
        CATEGORYID = "61dba35b-4f02-45c5-b648-c6badc0cbd79"
        params = [dict(name="@categoryId", value=CATEGORYID)]
        
        results = container.query_items(
            query=QUERY, parameters=params, enable_cross_partition_query=None
            )
        item_list = [item async for item in results]
        print("Item list", item_list)
# </async_code>

# (run_asyncode)
asyncio.run(manage_cosmos())
# (/run_asyncode)
