# Azure Cosmos DB for NoSQL client library samples for Python

[![Validate Python projects](https://github.com/Azure-Samples/cosmos-db-nosql-python-samples/actions/workflows/validate.yml/badge.svg)](https://github.com/Azure-Samples/cosmos-db-nosql-python-samples/actions/workflows/validate.yml)

## Getting started

This repo has a [devcontainer](https://containers.dev) environment making it easy to get started.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Azure-Samples/cosmos-db-nosql-python-samples?quickstart=1)

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

### Troubleshooting

If you use a self-signed certificate to connect your Cosmos DB instance (Cosmos-emulator, Docker image, proxy, ...), you can define your own certificate in the `REQUESTS_CA_BUNDLE` environment variable :

```bash
export REQUESTS_CA_BUNDLE='/etc/ssl/certs/emulatorcert.pem'
```
