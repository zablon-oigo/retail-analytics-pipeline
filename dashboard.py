import streamlit as st
from dotenv import load_dotenv
import os
from pyspark.sql import SparkSession
import pandas as pd
import plotly.express as px 

load_dotenv()

BUCKET = os.getenv("S3_BUCKET")
WAREHOUSE_PATH = f"s3a://{BUCKET}/iceberg-warehouse/"


@st.cache_resource
def get_spark():
    spark_builder = SparkSession.builder \
        .appName("Retail-Iceberg-Streamlit") \
        .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkCatalog") \
        .config("spark.sql.catalog.spark_catalog.type", "hadoop") \
        .config("spark.sql.catalog.spark_catalog.warehouse", WAREHOUSE_PATH) \
        .config("spark.sql.defaultCatalog", "spark_catalog") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.fast.upload", "true") \
        .config("spark.hadoop.fs.s3a.connection.maximum", "500") \

    return spark_builder.getOrCreate()

spark = get_spark()

