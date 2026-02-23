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

bucket = os.getenv("S3_BUCKET")
prefix = os.getenv("S3_STAGING_PREFIX")
file_name = os.getenv("CSV_FILE")
csv_path = f"s3a://{bucket}/{prefix}/{file_name}"

df = spark.read.option("header", "true").option("inferSchema", "true").csv(csv_path)


df = df.withColumn("InvoiceDate", to_timestamp(col("InvoiceDate"), "yyyy-MM-dd HH:mm:ss")) \
       .withColumnRenamed("Customer ID", "CustomerID")  


df = df.withColumn("year", year(col("InvoiceDate"))) \
       .withColumn("month", month(col("InvoiceDate")))
table_name = "spark_catalog.default.retail_iceberg" 

df.writeTo(table_name) \
    .using("iceberg") \
    .partitionedBy("year", "month") \
    .option("write.format.default", "parquet") \
    .option("check-ordering", "false") \
    .createOrReplace()

spark.sql(f"SELECT COUNT(*) FROM {table_name}").show()
spark.sql(f"DESCRIBE EXTENDED {table_name}").show(truncate=False) 


spark.stop()

print("Retail data successfully loaded into Iceberg table")
