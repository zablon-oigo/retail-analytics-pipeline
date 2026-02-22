import os
from dotenv import load_dotenv
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, year, month
load_dotenv()

spark = SparkSession.builder \
    .appName("RetailCSVtoIceberg") \
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.spark_catalog.type", "hadoop") \
    .config("spark.sql.defaultCatalog", "spark_catalog") \
    .getOrCreate()

spark.conf.set("spark.sql.parquet.compression.codec", "gzip") 

