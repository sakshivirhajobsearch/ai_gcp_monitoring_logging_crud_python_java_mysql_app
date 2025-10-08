import pandas as pd

def analyze_monitoring_data(data):
    if not data:
        return {"message": "No monitoring data found."}
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    summary = {
        "min": df['value'].min(),
        "max": df['value'].max(),
        "mean": df['value'].mean(),
        "std_dev": df['value'].std()
    }
    spikes = df[df['value'] > summary['mean'] + 2 * summary['std_dev']]
    summary["spike_count"] = len(spikes)
    summary["spike_samples"] = spikes.to_dict(orient='records')[:5]
    return summary

def analyze_logging_data(logs):
    if not logs:
        return {"message": "No logs to analyze."}
    df = pd.DataFrame(logs)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['severity'] = df['severity'].fillna("DEFAULT")
    severity_counts = df['severity'].value_counts().to_dict()
    keywords = ["error", "fail", "exception", "timeout", "crash"]
    anomaly_logs = df[df['text_payload'].str.contains('|'.join(keywords), case=False, na=False)]
    return {
        "severity_counts": severity_counts,
        "anomaly_count": len(anomaly_logs),
        "anomaly_samples": anomaly_logs[['log_name', 'severity', 'text_payload', 'timestamp']].head(5).to_dict(orient='records')
    }
