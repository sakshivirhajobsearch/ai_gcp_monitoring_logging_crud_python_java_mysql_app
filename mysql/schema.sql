CREATE DATABASE ai_gcp_monitoring_logging;

use ai_gcp_monitoring_logging;

CREATE TABLE monitoring_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    metric_name VARCHAR(255),
    value DOUBLE,
    timestamp DATETIME
);

CREATE TABLE logging_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    log_name VARCHAR(255),
    severity VARCHAR(50),
    text_payload TEXT,
    timestamp DATETIME
);
