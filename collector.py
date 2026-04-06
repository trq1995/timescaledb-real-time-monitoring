import psycopg2
import psutil
import time
from datetime import datetime

conn = psycopg2.connect(
    host="kg6knzxsi9.n6ykf4ibt5.tsdb.cloud.timescale.com",
    port=37773,
    dbname="tsdb",
    user="tsdbadmin",
    password="o0fzy8v2kmxlwubi",
    sslmode="require"
)

while True:
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    cur = conn.cursor()
    cur.execute("""
        INSERT INTO system_metrics (time, host, cpu_usage, memory_usage, disk_usage)
        VALUES (%s, %s, %s, %s, %s)
    """, (datetime.utcnow(), "my-pc", cpu, memory, disk))

    conn.commit()

    print("Data sent:", cpu, memory, disk)

    time.sleep(5)