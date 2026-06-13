# Blood-Supply-Intelligence Platform

## Overview

The Real-Time Blood Supply Intelligence Platform is an end-to-end streaming data engineering project that simulates blood inventory and demand events, processes them through a Medallion Architecture (Bronze, Silver, Gold), and delivers operational insights through Power BI dashboards.

The platform leverages Apache Kafka for event streaming, PySpark Structured Streaming for real-time processing, Delta Lake for reliable storage, Docker for containerization, and Power BI for analytics visualization.

## Architecture

```text
Blood Event Generator
        │
        ▼
Apache Kafka
        │
        ▼
PySpark Structured Streaming
        │
        ▼
Bronze Layer (Raw Events)
        │
        ▼
Silver Layer (Validated & Cleaned Data)
        │
        ▼
Gold Layer (Business Aggregations)
        │
        ▼
Power BI Dashboard
```

---

## Tech Stack

| Category          | Technologies                                  |
| ----------------- | --------------------------------------------- |
| Streaming         | Apache Kafka                                  |
| Processing        | PySpark Structured Streaming                  |
| Storage           | Delta Lake                                    |
| Containerization  | Docker, Docker Compose                        |
| Programming       | Python                                        |
| Analytics         | Power BI                                      |
| Data Architecture | Medallion Architecture (Bronze, Silver, Gold) |

---

## Project Objectives

* Simulate real-time blood inventory events.
* Process streaming data using Apache Spark.
* Implement Medallion Architecture using Delta Lake.
* Generate operational metrics for blood inventory management.
* Visualize insights using Power BI dashboards.

---

## Dataset

The simulated dataset contains blood inventory events with attributes such as:

* Event ID
* Timestamp
* Blood Type
* City
* Current Inventory
* Units Used
* Inventory Status
* Hospital Information

The generator continuously produces events to emulate real-world blood bank operations.

---

## Data Pipeline

### Bronze Layer

Purpose:
Store raw streaming events received from Kafka.

Operations:

* Kafka ingestion
* JSON parsing
* Schema enforcement
* Raw Delta Lake storage

Output:

```text
/data/bronze
```

---

### Silver Layer

Purpose:
Create validated and cleaned datasets.

Operations:

* Data quality checks
* Null handling
* Type validation
* Inventory status classification

Output:

```text
/data/silver
```

---

### Gold Layer

Purpose:
Generate business-ready aggregated metrics.

Aggregations:

* Average Inventory
* Total Units Used
* Event Counts
* Inventory Status Distribution
* Blood Type Analytics

Output:

```text
/data/gold
```

Example Gold Schema:

| Column           | Description              |
| ---------------- | ------------------------ |
| blood_type       | Blood group              |
| city             | City                     |
| inventory_status | HEALTHY / LOW / CRITICAL |
| avg_inventory    | Average inventory level  |
| total_units_used | Total units consumed     |
| event_count      | Number of events         |

---

## Power BI Dashboard

The dashboard provides real-time operational visibility through:

### KPI Cards

* Total Units Used
* Total Events
* Average Inventory

### Visualizations

* Blood Usage by Blood Type
* Inventory Status Distribution
* Average Inventory by Blood Type
* Blood Inventory Monitoring Table

---

## Project Structure

```text
real-time-blood-supply-intelligence/
│
├── simulator/
│   └── generate_blood_events.py
│
├── spark/
│   ├── 01_stream_blood_events_to_bronze.py
│   ├── 02_cleaned_values_silver.py
│   └── 03_aggregated_to_gold.py
│
├── data/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── powerbi/
│
├── sql/
│   └── create_tables.sql
│
├── docker-compose.yml
│
└── requirements.txt
```

---

## Key Features

* Real-time event ingestion using Apache Kafka
* Structured Streaming with PySpark
* Delta Lake implementation for reliable storage
* Medallion Architecture design pattern
* Containerized deployment with Docker
* Power BI analytics dashboard
* End-to-end streaming data pipeline

---

## Results

Successfully developed a real-time data engineering platform capable of:

* Processing continuous blood inventory events
* Maintaining Bronze, Silver, and Gold data layers
* Generating operational KPIs
* Supporting inventory monitoring and shortage analysis
* Delivering analytics through Power BI dashboards

---

## Future Enhancements

* PostgreSQL Data Warehouse Integration
* Apache Airflow Pipeline Orchestration
* Cloud Deployment on Azure or AWS
* Real-Time Dashboard Refresh
* Data Quality Monitoring Framework
* Alerting for Critical Blood Shortages

---

## Author
Hariharan Nadanasabapathi
