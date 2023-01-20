# <imports>
import os
import json

from azure.cosmos import CosmosClient, PartitionKey

# </imports>

# <environment_variables>
ENDPOINT = os.environ["COSMOS_ENDPOINT"]
KEY = os.environ["COSMOS_KEY"]
# </environment_variables>

# <constants>
DATABASE_NAME = "cosmicworks"
CONTAINER_NAME = "products"
# </constants>

# <create_client>
client = CosmosClient(url=ENDPOINT, credential=KEY)
# </create_client>

# <create_database>
database = client.create_database_if_not_exists(id=DATABASE_NAME)
print("Database\t", database.id)
# </create_database>

# <create_partition_key>
key_path = PartitionKey(path="/categoryId")
# </create_partition_key>

# <create_container>
container = database.create_container_if_not_exists(
    id=CONTAINER_NAME, partition_key=key_path, offer_throughput=400
)
print("Container\t", container.id)
# </create_container>

# <new_item>
new_item = {
    "id": "70b63682-b93a-4c77-aad2-65501347265f",
    "categoryId": "61dba35b-4f02-45c5-b648-c6badc0cbd79",
    "categoryName": "gear-surf-surfboards",
    "name": "Yamba Surfboard",
    "quantity": 12,
    "sale": False,
}
# </new_item>

# <create_item>
container.create_item(new_item)
# </create_item>

# <read_item>
existing_item = container.read_item(
    item="70b63682-b93a-4c77-aad2-65501347265f",
    partition_key="61dba35b-4f02-45c5-b648-c6badc0cbd79",
)
print("Point read\t", existing_item["name"])
# </read_item>

# <build_query>
QUERY = "SELECT * FROM products p WHERE p.categoryId = @categoryId"
CATEGORYID = "61dba35b-4f02-45c5-b648-c6badc0cbd79"
params = [dict(name="@categoryId", value=CATEGORYID)]
# </build_query>

# <query_items>
results = container.query_items(
    query=QUERY, parameters=params, enable_cross_partition_query=False
)
# </query_items>

# <iterate_query_results>
items = [item for item in results]
output = json.dumps(items, indent=True)
print("Result list\t", output)
# </iterate_query_results>
