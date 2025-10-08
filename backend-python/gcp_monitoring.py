from google.cloud import monitoring_v3, logging
from google.oauth2 import service_account

# Path to your service account JSON
SERVICE_ACCOUNT_FILE = "service_account.json"
PROJECT_ID = "adroit-standard-431618-m4"

# Load credentials
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)

# Function to list metrics
def list_metrics(project_id=PROJECT_ID, credentials=credentials):
    client = monitoring_v3.MetricServiceClient(credentials=credentials)
    project_name = f"projects/{project_id}"
    return [descriptor.type for descriptor in client.list_metric_descriptors(name=project_name)]

# Function to list logs (fixed)
def list_logs(project_id=PROJECT_ID, credentials=credentials):
    client = logging.Client(credentials=credentials, project=project_id)
    # Fetch log names from log entries
    logs = set()
    for entry in client.list_entries():
        logs.add(entry.log_name)
    return list(logs)
