import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = (
    SparkSession.builder
    .appName("BloodBronze")
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

schema = StructType([
    StructField("event_id", StringType()),
    StructField("timestamp", StringType()),
    StructField("blood_bank", StringType()),
    StructField("hospital", StringType()),
    StructField("blood_type", StringType()),
    StructField("units_received", IntegerType()),
    StructField("units_used", IntegerType()),
    StructField("current_inventory", IntegerType()),
    StructField("emergency_request", BooleanType()),
    StructField("city", StringType()),
    StructField("state", StringType())
])

raw_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:29092")
    .option("subscribe", "blood-events")
    .load()
)

bronze_df = (
    raw_df
    .selectExpr("CAST(value AS STRING)")
    .select(
        from_json(col("value"), schema).alias("data")
    )
    .select("data.*")
)

(
    bronze_df.writeStream
    .format("delta")
    .outputMode("append")
    .option(
        "checkpointLocation",
        "s3a://blood-supply-intelligence-lakehouse/checkpoints/bronze"
    )
    .start(
        "s3a://blood-supply-intelligence-lakehouse/bronze"
    )
    .awaitTermination()
)
