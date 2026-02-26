## Retail Lakehouse Pipeline

In this project, we take raw, messy CSV files stored in a data lake and transform them into a columnar, query-friendly format using Apache Iceberg tables. The data is stored in Parquet format and partitioned by year and month to make analytics queries faster and more efficient.

All transformations are performed using Apache Spark, which can scale to handle large datasets. Finally, the cleaned and structured data is made available for analytics and visualization using a Streamlit dashboard.

#### Architecture Diagram


#### Prerequisites

Before running the project, ensure you have the following installed:

|  Tool | Versions  | Purpose   |
|-------|-----------|-----------|
| Java  |  17+      |  Runtime for Spark |
| Python| 3.9+      | Running Pyspark |
| Spark |  4.0.0+   |   Distributed Data Processing |
| ICEBERG |  Latest    |  Table Format|
| Streamlit |  Latest    |  Visualization |

#### Dataset

The dataset can be dowloaded in kaggle the stored in s3:

```sh
aws s3 cp s3://your-s3-bucket/retail.csv - | head -n 4
```

#### Environment Variables

Create a .env file:

```sh
BUCKET=your_s3_bucket
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=your_region
```

#### Setup Guide
1. Clone the project
```sh
https://github.com/zablon-oigo/retail-analytics-pipeline.git
```
2. Change directory

```sh
cd retail-analytics-pipeline
```
3. Run Spark Cluster
```sh
spark-submit --master spark://svr:7077   --executor-memory 512m   --executor-cores 1   --num-executors 1   main.py
```
4. Set Up Dashboard
```sh
streamlit run dashboard.py
```