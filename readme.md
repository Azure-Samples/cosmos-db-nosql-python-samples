# Azure Cosmos DB for NoSQL client library samples for Python

## Getting started

This repo has a prebuilt development environment making it easy to get started.

### Pull the repo

Open the repo in a [development container](https://containers.dev) using either Visual Studio Code or GitHub Codespaces.

- **Visual Studio Code**: Clone this repo to your local machine and open the folder using the [Dev containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

- **GitHub Codespaces**: Open this repo in the browser with a [GitHub codespace](https://docs.github.com/en/codespaces/overview).

### Run the app

Configure your Azure Cosmos DB credentials as environment variables.

```bash
export COSMOS_ENDPOINT="<cosmos-account-URI>"
export COSMOS_KEY="<cosmos-account-PRIMARY-KEY>"
```

> **💡 TIP**: If you don't have an Azure Cosmos DB account, [create a free account](https://cosmos.azure.com/try/).

Run the quickstart sample app using the [`azure-cosmos`](https://pypi.org/project/azure-cosmos/) package from PyPI.

```bash
pip install azure-cosmos
python 001-quickstart/app.py
```

The application should output a single JSON object.

```json
{
  "id": "70b63682-b93a-4c77-aad2-65501347265f",
  "categoryId": "61dba35b-4f02-45c5-b648-c6badc0cbd79",
  "categoryName": "gear-surf-surfboards",
  "name": "Yamba Surfboard",
  "quantity": 12,
  "sale": false,
  "_rid": "yzN6AIfJxe0BAAAAAAAAAA==",
  "_self": "dbs/yzN6AA==/colls/yzN6AIfJxe0=/docs/yzN6AIfJxe0BAAAAAAAAAA==/",
  "_etag": "\"2a00ccd4-0000-0200-0000-63650e420000\"",
  "_attachments": "attachments/",
  "_ts": 16457527130
}
```

> **💡 TIP**: The fields assigned by Azure Cosmos DB (ex. `id`) will vary from this sample output.

### Validate any changes you make

If you change the code, run the linter and code formatter.

```bash
pip install flake8
flake8 --verbose 001-quickstart/app.py
```

```bash
pip install black
black --verbose 001-quickstart/app.py
```

## Samples

This project contains multiple samples used in [Azure Cosmos DB for NoSQL](https://learn.microsoft.com/azure/cosmos-db/nosql/) documentation.

| Sample | Documentation |
| --- | --- |
| [001-quickstart](001-quickstart/app.py) | [Quickstart: Azure Cosmos DB for NoSQL client library for Python](https://learn.microsoft.com/azure/cosmos-db/nosql/quickstart-python?tabs=azure-portal%2Clinux%2Csync) |
| [002-quickstart-async](002-quickstart-async/app.py) | [Quickstart: Azure Cosmos DB for NoSQL client library for Python](https://learn.microsoft.com/azure/cosmos-db/nosql/quickstart-python?tabs=azure-portal%2Clinux%2Casync) |
| [[003-how-to](003-how-to/app.py)] | [Get started with Azure Cosmos DB for NoSQL using Python](https://learn.microsoft.com/azure/cosmos-db/nosql/how-to-python-get-started) |
| [[004-create-db](003-how-to/app.py)] | [Create a database in Azure Cosmos DB for NoSQL using Python](https://learn.microsoft.com/azure/cosmos-db/nosql/how-to-python-create-database) |
| [[005-create-container](003-how-to/app.py)] | [Create a container in Azure Cosmos DB for NoSQL using Python](https://learn.microsoft.com/azure/cosmos-db/nosql/how-to-python-create-container) |
