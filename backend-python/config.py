import os

# ✅ MySQL connection configuration
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',  # Change as per your setup
    'database': 'ai_gcp_monitoring_logging'
}

# ✅ Lazy-load GCP credentials only when needed
def get_gcp_credentials():
    from google.oauth2 import service_account
    GCP_KEY_FILE = os.getenv("GCP_KEY_FILE", "service_account.json")
    return service_account.Credentials.from_service_account_file(GCP_KEY_FILE)
