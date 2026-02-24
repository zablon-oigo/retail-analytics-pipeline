## Retail Lakehouse Pipeline

In this project, we take raw, messy CSV files stored in a data lake and transform them into a columnar, query-friendly format using Apache Iceberg tables. The data is stored in Parquet format and partitioned by year and month to make analytics queries faster and more efficient.

All transformations are performed using Apache Spark, which can scale to handle large datasets. Finally, the cleaned and structured data is made available for analytics and visualization using a Streamlit dashboard.

#### Architecture Diagram


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