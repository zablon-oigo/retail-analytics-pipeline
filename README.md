## Retail Lakehouse Pipeline

In this project, we take raw, messy CSV files stored in a data lake and transform them into a columnar, query-friendly format using Apache Iceberg tables. The data is stored in Parquet format and partitioned by year and month to make analytics queries faster and more efficient.

All transformations are performed using Apache Spark, which can scale to handle large datasets. Finally, the cleaned and structured data is made available for analytics and visualization using a Streamlit dashboard.