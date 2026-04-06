# 🚀 Real-Time System Monitoring using TimescaleDB

This project is a real-time system monitoring application built using **PostgreSQL + TimescaleDB**. It collects system metrics such as CPU, memory, and disk usage, stores them as time-series data, and visualizes trends using a dashboard.

---

## 🎯 Features

- Collect real-time system metrics using Python
- Store data in TimescaleDB hypertables
- Perform time-series analysis using SQL (`time_bucket`)
- Visualize data using Streamlit dashboard
- Identify performance trends and bottlenecks

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
