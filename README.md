# 🚀 Real-Time System Monitoring using TimescaleDB

This project is a real-time system monitoring application built using **PostgreSQL + TimescaleDB**. It collects system metrics such as CPU, memory, and disk usage, stores them as time-series data, and visualizes trends using a dashboard.

---

##  🚀 Features

- 📊 **Real-Time Monitoring**  
  Collects live system metrics including CPU, memory, and disk usage at regular intervals.

- 🗄️ **Time-Series Storage (TimescaleDB)**  
  Stores data in hypertables optimized for time-series workloads, enabling efficient querying and scalability.

- ⚡ **SQL-Based Analytics**  
  Uses advanced SQL functions like `time_bucket` for time-based aggregation and trend analysis.

- 📈 **Interactive Dashboard**  
  Visualizes system metrics using a Streamlit dashboard with real-time charts and summaries.

- 🚨 **Threshold-Based Alerts**  
  Detects high resource usage (e.g., CPU > 80%) and displays alerts in the dashboard for proactive monitoring.

- 🔍 **Performance Analysis**  
  Enables identification of system bottlenecks using query-based insights and historical trends.

- ☁️ **Cloud Integration**  
  Connects to Timescale Cloud (Tiger Data) for managed PostgreSQL and production-like environment.

- 🧠 **Real-World Use Case**  
  Demonstrates how time-series databases are used in monitoring, DevOps, and analytics systems.
🔥 Short Version (for GitHub description box)
Real-time monitoring system using TimescaleDB with hypertables, SQL analytics, Streamlit dashboard, and threshold-based alerting (CPU > 80%).

---

## 🛠️ Tech Stack

- PostgreSQL (TimescaleDB)
- Python (psycopg2, psutil)
- Streamlit (Dashboard)
- SQL (CTEs, Aggregations)

---

## ⚙️ Setup Instructions

### 1. Install dependencies
```bash
python -m pip install -r requirements.txt







