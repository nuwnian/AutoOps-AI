import os
import sys
import requests
from azure.identity import ClientSecretCredential
from azure.mgmt.web import WebSiteManagementClient

def is_healthy(health_url):
    try:
        response = requests.get(health_url, timeout=10)
        response.raise_for_status()
        if response.text.strip().lower() == "ok":
            print("App is healthy.")
            return True
        print(f"/health returned: {response.text}")
        return False
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def restart_app(credential, subscription_id, resource_group, web_app_name):
    try:
        web_client = WebSiteManagementClient(credential, subscription_id)
        print("Restarting Azure Web App...")
        web_client.web_apps.restart(resource_group, web_app_name)
        print("Restart command sent.")
    except Exception as e:
        print(f"Failed to restart app: {e}")

def main():
    required_env = [
        "AZURE_CLIENT_ID", "AZURE_CLIENT_SECRET", "AZURE_TENANT_ID",
        "AZURE_SUBSCRIPTION_ID", "RESOURCE_GROUP", "WEB_APP_NAME", "HEALTH_URL"
    ]
    for var in required_env:
        if not os.getenv(var):
            print(f"Missing required environment variable: {var}")
            sys.exit(1)
    credential = ClientSecretCredential(
        tenant_id=os.environ["AZURE_TENANT_ID"],
        client_id=os.environ["AZURE_CLIENT_ID"],
        client_secret=os.environ["AZURE_CLIENT_SECRET"],
    )
    subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
    resource_group = os.environ["RESOURCE_GROUP"]
    web_app_name = os.environ["WEB_APP_NAME"]
    health_url = os.environ["HEALTH_URL"]

    if not is_healthy(health_url):
        restart_app(credential, subscription_id, resource_group, web_app_name)
    else:
        print("No action needed.")

if __name__ == "__main__":
    main()