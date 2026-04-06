import streamlit as st
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="kg6knzxsi9.n6ykf4ibt5.tsdb.cloud.timescale.com",
    port=37773,   # use your actual port
    dbname="tsdb",
    user="tsdbadmin",
    password="o0fzy8v2kmxlwubi",
    sslmode="require"
)

st.set_page_config(page_title="System Monitoring Dashboard", layout="wide")
st.title("Real-Time System Monitoring Dashboard")

# latest records
latest_query = """
SELECT time, host, cpu_usage, memory_usage, disk_usage
FROM system_metrics
ORDER BY time DESC
LIMIT 20;
"""

# cpu trend
cpu_query = """
SELECT time_bucket('1 minute', time) AS minute,
       avg(cpu_usage) AS avg_cpu
FROM system_metrics
GROUP BY minute
ORDER BY minute;
"""

# memory trend
memory_query = """
SELECT time_bucket('1 minute', time) AS minute,
       avg(memory_usage) AS avg_memory
FROM system_metrics
GROUP BY minute
ORDER BY minute;
"""

# disk trend
disk_query = """
SELECT time_bucket('1 minute', time) AS minute,
       avg(disk_usage) AS avg_disk
FROM system_metrics
GROUP BY minute
ORDER BY minute;
"""

latest_df = pd.read_sql(latest_query, conn)
cpu_df = pd.read_sql(cpu_query, conn)
memory_df = pd.read_sql(memory_query, conn)
disk_df = pd.read_sql(disk_query, conn)

# latest values
if not latest_df.empty:
    newest = latest_df.iloc[0]
    c1, c2, c3 = st.columns(3)
    c1.metric("CPU Usage", f"{newest['cpu_usage']:.2f}%")
    c2.metric("Memory Usage", f"{newest['memory_usage']:.2f}%")
    c3.metric("Disk Usage", f"{newest['disk_usage']:.2f}%")

st.subheader("CPU Usage Trend")
if not cpu_df.empty:
    st.line_chart(cpu_df.set_index("minute")["avg_cpu"])

st.subheader("Memory Usage Trend")
if not memory_df.empty:
    st.line_chart(memory_df.set_index("minute")["avg_memory"])

st.subheader("Disk Usage Trend")
if not disk_df.empty:
    st.line_chart(disk_df.set_index("minute")["avg_disk"])

st.subheader("Latest Metrics")
st.dataframe(latest_df, use_container_width=True)

conn.close()