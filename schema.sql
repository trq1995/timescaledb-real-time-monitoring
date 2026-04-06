CREATE EXTENSION IF NOT EXISTS timescaledb;

CREATE TABLE system_metrics (
    time TIMESTAMPTZ NOT NULL,
    host TEXT,
    cpu_usage DOUBLE PRECISION,
    memory_usage DOUBLE PRECISION,
    disk_usage DOUBLE PRECISION
);

SELECT create_hypertable('system_metrics', 'time');

CREATE INDEX ON system_metrics (time DESC);
CREATE INDEX ON system_metrics (host, time DESC);