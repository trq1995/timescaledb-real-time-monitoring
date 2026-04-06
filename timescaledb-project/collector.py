import psycopg2
import psutil
import time
from datetime import datetime
import socket

conn = psycopg2.connect(
    host="YOUR_HOST",
    port=YOUR_PORT,
    dbname="YOUR_DB",
    user="YOUR_USER",
    password="YOUR_PASSWORD",
    sslmode="require"
)

host = socket.gethostname()

while True:
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    cur = conn.cursor()
    cur.execute("""
        INSERT INTO system_metrics (time, host, cpu_usage, memory_usage, disk_usage)
        VALUES (%s, %s, %s, %s, %s)
    """, (datetime.utcnow(), host, cpu, memory, disk))

    conn.commit()
    print("Inserted:", cpu, memory, disk)

    time.sleep(5)
