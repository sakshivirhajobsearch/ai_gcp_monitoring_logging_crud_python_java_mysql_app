import mysql.connector
from config import MYSQL_CONFIG
from datetime import datetime

try:
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()

    # Dummy monitoring data
    cursor.execute("""
        INSERT INTO monitoring_metrics (metric_type, value, timestamp, ai_analysis)
        VALUES (%s, %s, %s, %s)
    """, (
        "compute.googleapis.com/instance/cpu/utilization",
        0.47,
        datetime.utcnow(),
        "CPU utilization is within normal range."
    ))

    # Dummy log data
    cursor.execute("""
        INSERT INTO stackdriver_logs (log_message, timestamp, ai_analysis)
        VALUES (%s, %s, %s)
    """, (
        "Instance i-123456 restarted unexpectedly.",
        datetime.utcnow(),
        "Potential issue detected: unexpected instance restart."
    ))

    conn.commit()
    print("✅ Dummy data inserted successfully.")

except mysql.connector.Error as err:
    print(f"❌ Error inserting dummy data: {err}")
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
