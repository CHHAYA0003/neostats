# Virtual Server Monitoring Pipeline

# Project Overview

This project demonstrates a **server monitoring data pipeline** built using **Python and Power BI**.
The pipeline ingests server log data from a CSV dataset, performs data cleaning and transformation, and visualizes key server performance metrics using an interactive Power BI dashboard.

The goal of this project is to monitor server health, detect performance bottlenecks, and provide data-driven insights for infrastructure monitoring.

# Dataset

File: `server_logs.csv`

Dataset Columns

| Column          | Description                            |
| --------------- | -------------------------------------- |
| Server_ID       | Unique identifier of the server        |
| Timestamp       | Time of recorded server activity       |
| CPU_Usage       | CPU utilization percentage             |
| Memory_Usage    | Memory consumption                     |
| Disk_IO         | Disk input/output activity             |
| Network_IO      | Network traffic activity               |
| Server_Location | Location of the server                 |
| OS_Type         | Operating system running on the server |
| Instance_Size   | Server configuration size              |


# Data Pipeline Architecture

The project follows a structured data pipeline workflow:

1. **Data Ingestion**
   Load server monitoring data from CSV files.

2. **Data Cleaning & Preprocessing**
   Handle missing values and ensure data consistency.

3. **Feature Engineering**
   Generate useful metrics for performance analysis.

4. **Data Storage**
   Store processed data in **Azure SQL Database / Azure Data Lake**.


# Power BI Dashboard

The Power BI dashboard provides insights into server performance metrics.

Visualizations Included

* CPU Utilization Trend
* Memory Usage Analysis
* Server Uptime Monitoring
* Resource Utilization Overview

Interactive filters allow analysis based on location, server type, and performance metrics.

# Tools & Technologies

* Python
* Pandas
* Azure SQL / Azure Data Lake
* Power BI

# Project Structure

server-monitoring-pipeline

│
├── data_pipeline.ipynb
├── server_logs.csv
├── Server_Monitoring_Dashboard.pbix
├── Documentation.pdf
└── Presentation.pptx

## Conclusion

This project demonstrates how data engineering pipelines can be used to process server monitoring data and create actionable insights using Power BI dashboards.
The approach enables better infrastructure monitoring and proactive performance management.
