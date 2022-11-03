from azure.cosmos import CosmosClient, PartitionKey

import os

endpoint = os.environ["COSMOS_ENDPOINT"]
key = os.environ["COSMOS_KEY"]

client = CosmosClient(url=endpoint, credential=key)

database = client.create_database_if_not_exists(id="adventureworks")

partitionKeyPath = PartitionKey(path="/categoryId")

container = database.create_container_if_not_exists(
    id="products", partition_key=partitionKeyPath, offer_throughput=400
)
