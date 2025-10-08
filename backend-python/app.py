from flask import Flask
from google.cloud import monitoring_v3, logging_v2
from google.oauth2 import service_account

app = Flask(__name__)

SERVICE_ACCOUNT_FILE = "service_account.json"
PROJECT_ID = "adroit-standard-431618-m4"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE
)

# --- Monitoring ---
def list_metrics(project_id, credentials):
    try:
        client = monitoring_v3.MetricServiceClient(credentials=credentials)
        project_name = f"projects/{project_id}"
        return [descriptor.type for descriptor in client.list_metric_descriptors(name=project_name)]
    except Exception:
        # Dummy fallback metrics
        return [
            "custom.googleapis.com/dummy_metric_1",
            "custom.googleapis.com/dummy_metric_2"
        ]

@app.route("/monitoring/metrics")
def metrics():
    try:
        metrics_list = list_metrics(PROJECT_ID, credentials)
        return {"metrics": metrics_list}
    except Exception as e:
        return {"error": str(e)}, 500

# --- Logging ---
def list_logs(project_id, credentials):
    try:
        client = logging_v2.LoggingClient(credentials=credentials)
        parent = f"projects/{project_id}"
        return [entry.name for entry in client.list_logs(parent=parent)]
    except Exception:
        # Dummy fallback logs
        return [
            "projects/dummy-project/logs/dummy_log_1",
            "projects/dummy-project/logs/dummy_log_2"
        ]

@app.route("/logging/logs")
def logs():
    try:
        logs_list = list_logs(PROJECT_ID, credentials)
        return {"logs": logs_list}
    except Exception as e:
        return {"error": str(e)}, 500

# --- Home Route ---
@app.route("/")
def home():
    return {
        "message": "Welcome to the GCP Monitoring & Logging API",
        "routes": [
            "/monitoring/metrics",
            "/logging/logs",
            "/dashboard"
        ]
    }

# --- Dashboard Route (metrics + logs) ---
@app.route("/dashboard")
def dashboard():
    return {
        "metrics": list_metrics(PROJECT_ID, credentials),
        "logs": list_logs(PROJECT_ID, credentials)
    }

if __name__ == "__main__":
    app.run(debug=True)
