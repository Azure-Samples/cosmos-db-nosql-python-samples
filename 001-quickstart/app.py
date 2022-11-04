# <imports>
from azure.cosmos import CosmosClient, PartitionKey

# </imports>

# <environment_variables>
import os

endpoint = os.environ["COSMOS_ENDPOINT"]
key = os.environ["COSMOS_KEY"]
# </environment_variables>

# <create_client>
client = CosmosClient(url=endpoint, credential=key)
# </create_client>

# <create_database>
database = client.create_database_if_not_exists(id="adventureworks")
# </create_database>

# <create_partition_key>
partitionKeyPath = PartitionKey(path="/categoryId")
# </create_partition_key>

# <create_container>
container = database.create_container_if_not_exists(
    id="products", partition_key=partitionKeyPath, offer_throughput=400
)
# </create_container>
