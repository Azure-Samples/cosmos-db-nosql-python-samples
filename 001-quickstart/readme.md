# Quickstart 001 samples

There are three sample apps in this directory:

* *app.py* expects environment variables: COSMOS_ENDPOINT, COSMOS_KEY. DATABASE_NAME and CONTAINER_NAME are constants defined in the code. If the database and collection don't exist, they are created.

* *app_conn.py* is the same as *app.py*, except the code assumes the database and collection already exist. For example, if you already created the database and collection using the Azure portal or Azure CLI.

* *app_cred.py* expects only the environment variable: COSMOS_ENDPOINT. DATABASE_NAME and CONTAINER_NAME are constants defined in the code. The code assumes the database and collection already exist. Authentication is passwordless, that is, with `DefaultAzureCredential`. Passwordless authentication requires the Azure CLI and that you are logged in with your account. This is the recommended approach.

Many of the samples in this directory supply the code snippets for documentation, Keep that in mind when making changes.
