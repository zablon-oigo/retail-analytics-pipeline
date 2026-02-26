## Retail Lakehouse Analytics Pipeline

This project demonstrates how to build a modern Lakehouse architecture using Apache Spark, Apache Iceberg, and Streamlit.

We ingest raw, messy CSV data stored in a data lake (Amazon S3), transform it into a clean and structured format using Apache Spark, and store it as Apache Iceberg tables backed by Parquet files.

The data is partitioned by year and month to optimize analytical queries. Finally, a Streamlit dashboard provides interactive analytics and insights.

#### Architecture Diagram


#### Flow Summary

1. Raw CSV stored in S3 (Data Lake)

2. Spark reads and transforms data

3. Cleaned data written as Iceberg tables (Parquet format)

4. Streamlit dashboard queries Iceberg tables

5. Users interact with analytics UI


#### Prerequisites

Before running the project, ensure you have the following installed:

|  Tool | Versions  | Purpose   |
|-------|-----------|-----------|
| Java  |  17+      | Required runtime for Spark |
| Python| 3.9+      | PySpark & dashboard |
| Spark |  4.0.0+   |  Distributed data processing|
| Iceberg |  Latest    |  Open table format|
| Streamlit |  Latest    | Analytics dashboard|
| AWS S3 |  ----   | Data lake storage|

#### Dataset

Download the dataset from Kaggle and upload it to your S3 bucket.

Verify upload:

```sh
aws s3 cp s3://your-s3-bucket/retail.csv - | head -n 4
```

#### Environment Configuration

Create a .env file in the project root:

```sh
BUCKET=your_s3_bucket
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=your_region
```

Make sure your Spark job loads these environment variables.

#### Setup & Run Guide

1. Clone the Repository
```sh
https://github.com/zablon-oigo/retail-analytics-pipeline.git
```

3. Start Spark Job

Submit the Spark transformation job:

```sh
spark-submit --master spark://svr:7077   --executor-memory 512m   --executor-cores 1   --num-executors 1   main.py
```
This will:

- Read raw CSV from S3
- Clean and transform data
- Write partitioned Iceberg tables in Parquet format


4. Launch the Dashboard
```sh
streamlit run dashboard.py
```
Open the browser URL shown in the terminal to access the analytics dashboard.