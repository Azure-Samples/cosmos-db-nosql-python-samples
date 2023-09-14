# <imports>
from azure.cosmos import CosmosClient, PartitionKey

# </imports>

# <client>
client = CosmosClient(
    url="<https://localhost:8081>",
    credential=(
        "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGG"
        "yPMbIZnqyMsEcaGQy67XIw/Jw=="
    ),
)
# </client>

# <resources>
database = client.create_database_if_not_exists(
    id="cosmicworks",
    offer_throughput=400,
)

container = database.create_container_if_not_exists(
    id="products",
    partition_key=PartitionKey(
        path="/id",
    ),
)
# </resources>

# <upsert>
item = {"id": "68719518370", "name": "Kiama classic surfboard"}

container.upsert_item(item)
# </upsert>
