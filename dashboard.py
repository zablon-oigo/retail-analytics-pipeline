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

st.set_page_config(page_title="Retail Dashboard", layout="wide")

st.title("Retail Sales Dashboard")
st.markdown("Data loaded from Apache Iceberg table on S3")

table_name = "spark_catalog.default.retail_iceberg"

with st.spinner("Reading Iceberg table..."):
    try:
        df_spark = spark.read.table(table_name)

        df_pd = df_spark.toPandas()  

        st.success(f"Loaded {len(df_pd):,} rows from Iceberg table!")

    except Exception as e:
        st.error(f"Error reading table: {e}")
        st.stop()


col1, col2 = st.columns(2)

with col1:
    countries = sorted(df_pd["Country"].dropna().unique())
    selected_countries = st.multiselect("Select Countries", countries, default=countries[:5])

with col2:
    years = sorted(df_pd["year"].dropna().unique())
    selected_years = st.multiselect("Select Years", years, default=years)


filtered_df = df_pd[
    df_pd["Country"].isin(selected_countries) &
    df_pd["year"].isin(selected_years)
]
