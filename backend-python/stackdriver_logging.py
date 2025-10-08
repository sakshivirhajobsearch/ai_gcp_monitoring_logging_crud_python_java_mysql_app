from google.cloud import logging_v2

def list_logs(project_id, credentials):
    client = logging_v2.LoggingServiceV2Client(credentials=credentials)
    parent = f"projects/{project_id}"
    logs = []
    for entry in client.list_log_entries({"resource_names": [parent]}):
        logs.append({
            "log_name": entry.log_name,
            "severity": entry.severity.name,
            "text_payload": entry.text_payload,
            "timestamp": entry.timestamp.ToDatetime().isoformat()
        })
    return logs
