SELECT time_bucket('1 minute', time), avg(cpu_usage)
FROM system_metrics
GROUP BY 1;

SELECT * FROM system_metrics ORDER BY time DESC LIMIT 10;

SELECT * FROM system_metrics WHERE cpu_usage > 80;
