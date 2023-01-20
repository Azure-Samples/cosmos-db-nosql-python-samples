# <imports>
import os
import json
import asyncio

from azure.cosmos.aio import CosmosClient
from azure.identity.aio import DefaultAzureCredential

# </imports>

# <environment_variables_and_credential>
ENDPOINT = os.environ["COSMOS_ENDPOINT"]
# </environment_variables_and_credential>

# <constants>
DATABASE_NAME = "cosmicworks"
CONTAINER_NAME = "products"
# </constants>

# <async_code>

async def manage_cosmos():

    async with DefaultAzureCredential() as credential:

        async with CosmosClient(url=ENDPOINT, credential=credential) as client:

            database = client.get_database_client(DATABASE_NAME)
            print("Database\t", database.id)

            container = database.get_container_client(CONTAINER_NAME)
            print("Container\t", container.id)

            new_item = {
                "id": "70b63682-b93a-4c77-aad2-65501347265f",
                "categoryId": "61dba35b-4f02-45c5-b648-c6badc0cbd79",
                "categoryName": "gear-surf-surfboards",
                "name": "Yamba Surfboard",
                "quantity": 12,
                "sale": False,
            }

            await container.create_item(new_item)

            existing_item = await container.read_item(
                item="70b63682-b93a-4c77-aad2-65501347265f",
                partition_key="61dba35b-4f02-45c5-b648-c6badc0cbd79",
            )
            print("Point read\t", existing_item["name"])

            QUERY = "SELECT * FROM products p WHERE p.categoryId = @categoryId"
            CATEGORYID = "61dba35b-4f02-45c5-b648-c6badc0cbd79"
            params = [dict(name="@categoryId", value=CATEGORYID)]

            results = container.query_items(
                query=QUERY, parameters=params, enable_cross_partition_query=False
            )
            items = [item async for item in results]
            output = json.dumps(items, indent=True)
            print("Result list\t", output)

# </async_code>

# (run_async_function)
asyncio.run(manage_cosmos())
# (/run_async_function)
