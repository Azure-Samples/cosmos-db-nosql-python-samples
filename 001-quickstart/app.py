# <imports>
import os
import json
from azure.cosmos import CosmosClient, PartitionKey

# </imports>

# <environment_variables>
endpoint = os.environ["COSMOS_ENDPOINT"]
key = os.environ["COSMOS_KEY"]
# </environment_variables>

# <create_client>
client = CosmosClient(url=endpoint, credential=key)
# </create_client>

# <create_database>
database = client.create_database_if_not_exists(id="cosmicworks")
# </create_database>

# <create_partition_key>
partitionKeyPath = PartitionKey(path="/categoryId")
# </create_partition_key>

# <create_container>
container = database.create_container_if_not_exists(
    id="products", partition_key=partitionKeyPath, offer_throughput=400
)
# </create_container>

# <new_item>
newItem = {
    "id": "70b63682-b93a-4c77-aad2-65501347265f",
    "categoryId": "61dba35b-4f02-45c5-b648-c6badc0cbd79",
    "categoryName": "gear-surf-surfboards",
    "name": "Yamba Surfboard",
    "quantity": 12,
    "sale": False,
}
# </new_item>

# <create_item>
container.create_item(newItem)
# </create_item>

# <read_item>
existingItem = container.read_item(
    item="70b63682-b93a-4c77-aad2-65501347265f",
    partition_key="61dba35b-4f02-45c5-b648-c6badc0cbd79",
)
# </read_item>

# <build_query>
QUERY = "SELECT * FROM products p WHERE p.categoryId = @categoryId"
CATEGORYID = "61dba35b-4f02-45c5-b648-c6badc0cbd79"
params = [dict(name="@categoryId", value=CATEGORYID)]
# </build_query>

# <query_items>
items = container.query_items(
    query=QUERY, parameters=params, enable_cross_partition_query=False
)
# </query_items>

# <iterate_query_results>
for item in items:
    print(json.dumps(item, indent=True))
# </iterate_query_results>
