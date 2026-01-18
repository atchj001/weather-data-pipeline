# Weather Data Pipeline

## Overview

This project is an end-to-end **data engineering pipeline** that ingests live weather data from an external API, stores raw records in a relational database, transforms the data into analytics-ready models, and visualises the results in a dashboard.

---

## Architecture

**Weather API → Python Ingestion → PostgreSQL (Raw) → Airflow → dbt → Superset**

- **Extract:** Python retrieves live weather data from an external API  
- **Load:** Raw records are inserted into PostgreSQL as a system of record  
- **Orchestrate:** Airflow schedules and controls the execution of ingestion and transformation steps  
- **Transform:** dbt applies SQL-based transformations inside the database  
- **Analytics:** Apache Superset visualises transformed tables in near real time  
- **Deploy:** All services run in Docker containers using Docker Compose  

---

## Tech Stack

- **Python** – API ingestion and database interaction  
- **PostgreSQL** – Raw and transformed data storage  
- **Apache Airflow** – Workflow orchestration and scheduling  
- **dbt** – Data modelling and transformations  
- **Apache Superset** – Analytics dashboards and visualisation  
- **Docker & Docker Compose** – Containerisation and reproducible environments  

---

## Data Pipeline Design

### Ingestion
- Data is fetched from a third-party weather API at a defined interval  
- Ingestion logic is intentionally lightweight and focused on reliability  

### Storage
- Raw data is stored without business transformations  
- This allows traceability and reprocessing if requirements change  

### Transformation
- dbt models create a staging layer to clean and standardise data  
- Reporting models aggregate data (for example daily averages) for analytics use cases  

### Orchestration
- Airflow ensures ingestion runs before transformations  
- Failures are logged and visible, preventing partial updates  

### Analytics
- Superset connects to transformed tables only  
- Dashboards can be configured to auto-refresh for near real-time reporting  

---

## Running the Project

### Prerequisites
- Docker  
- Docker Compose  

### Start the full pipeline
```bash
docker compose up

