import streamlit as st
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="kg6knzxsi9.n6ykf4ibt5.tsdb.cloud.timescale.com",
    port=37773,
    dbname="tsdb",
    user="tsdbadmin",
    password="o0fzy8v2kmxlwubi",
    sslmode="require"
)

st.set_page_config(page_title="System Monitoring Dashboard", layout="wide")
st.title("System Monitoring Dashboard")

cpu_query = """
SELECT time_bucket('1 minute', time) AS minute,
       avg(cpu_usage) AS cpu
FROM system_metrics
GROUP BY minute
ORDER BY minute;
"""

memory_query = """
SELECT time_bucket('1 minute', time) AS minute,
       avg(memory_usage) AS memory
FROM system_metrics
GROUP BY minute
ORDER BY minute;
"""

disk_query = """
SELECT time_bucket('1 minute', time) AS minute,
       avg(disk_usage) AS disk
FROM system_metrics
GROUP BY minute
ORDER BY minute;
"""

latest_query = """
SELECT time, host, cpu_usage, memory_usage, disk_usage
FROM system_metrics
ORDER BY time DESC
LIMIT 20;
"""

alerts_query = """
SELECT time, host, cpu_usage
FROM system_metrics
WHERE cpu_usage > 80
ORDER BY time DESC
LIMIT 20;
"""

df_cpu = pd.read_sql(cpu_query, conn)
df_mem = pd.read_sql(memory_query, conn)
df_disk = pd.read_sql(disk_query, conn)
df_latest = pd.read_sql(latest_query, conn)
df_alerts = pd.read_sql(alerts_query, conn)

if not df_latest.empty:
    latest = df_latest.iloc[0]
    c1, c2, c3 = st.columns(3)
    c1.metric("CPU Usage", f"{latest['cpu_usage']:.2f}%")
    c2.metric("Memory Usage", f"{latest['memory_usage']:.2f}%")
    c3.metric("Disk Usage", f"{latest['disk_usage']:.2f}%")

st.subheader("CPU Usage")
if not df_cpu.empty:
    st.line_chart(df_cpu.set_index("minute")["cpu"])

st.subheader("Memory Usage")
if not df_mem.empty:
    st.line_chart(df_mem.set_index("minute")["memory"])

st.subheader("Disk Usage")
if not df_disk.empty:
    st.line_chart(df_disk.set_index("minute")["disk"])

st.subheader("Alerts: CPU > 80%")
if not df_alerts.empty:
    st.error("High CPU usage detected")
    st.dataframe(df_alerts, use_container_width=True)
else:
    st.success("No high CPU alerts")

st.subheader("Latest Metrics")
st.dataframe(df_latest, use_container_width=True)

conn.close()