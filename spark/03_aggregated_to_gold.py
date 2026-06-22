import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = (
    SparkSession.builder
    .appName("BloodGold")
    .config(
        "spark.sql.extensions",
        "io.delta.sql.DeltaSparkSessionExtension"
    )
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog"
    )
    .config(
        "spark.hadoop.fs.s3a.impl",
        "org.apache.hadoop.fs.s3a.S3AFileSystem"
    )
    .config(
        "spark.hadoop.fs.s3a.access.key",
        os.getenv("AWS_ACCESS_KEY_ID")
    )
    .config(
        "spark.hadoop.fs.s3a.secret.key",
        os.getenv("AWS_SECRET_ACCESS_KEY")
    )
    .config(
        "spark.hadoop.fs.s3a.endpoint",
        "s3.us-east-2.amazonaws.com"
    )
    .getOrCreate()
)

silver_df = (
    spark.readStream
    .format("delta")
    .load(
        "s3a://blood-supply-intelligence-lakehouse/silver"
    )
)

gold_df = (
    silver_df
    .groupBy(
        "blood_type",
        "city",
        "inventory_status"
    )
    .agg(
        avg("current_inventory").alias("avg_inventory"),
        sum("units_used").alias("total_units_used"),
        count("*").alias("event_count")
    )
)

(
    gold_df.writeStream
    .format("delta")
    .outputMode("complete")
    .option(
        "checkpointLocation",
        "s3a://blood-supply-intelligence-lakehouse/checkpoints/gold"
    )
    .start(
        "s3a://blood-supply-intelligence-lakehouse/gold"
    )
    .awaitTermination()
)
