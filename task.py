from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, hour, to_timestamp, dense_rank
from pyspark.sql.window import Window

# Create Spark session
spark = SparkSession.builder.appName("IoT Sensor Data Analysis").getOrCreate()

# Task 1: Load & Basic Exploration
df = spark.read.csv("sensor_data.csv", header=True, inferSchema=True)
df.createOrReplaceTempView("sensor_readings")

# Show first 5 rows
df.show(5)

# Count total records
print("Total records:", df.count())

# Distinct locations or sensor types
df.select("location").distinct().show()
df.select("sensor_type").distinct().show()

# Save one output to task1_output.csv
df.limit(5).toPandas().to_csv("task1_output.csv", index=False)


# Task 2: Filtering & Simple Aggregations
in_range = df.filter((col("temperature") >= 18) & (col("temperature") <= 30))
out_of_range = df.filter((col("temperature") < 18) | (col("temperature") > 30))

print("In-range count:", in_range.count())
print("Out-of-range count:", out_of_range.count())

agg_df = df.groupBy("location").agg(
    avg("temperature").alias("avg_temperature"),
    avg("humidity").alias("avg_humidity")
).orderBy(col("avg_temperature").desc())

agg_df.show()
agg_df.toPandas().to_csv("task2_output.csv", index=False)


# Task 3: Time-Based Analysis
df = df.withColumn("timestamp", to_timestamp("timestamp"))
df.createOrReplaceTempView("sensor_readings")

df_hourly = df.withColumn("hour_of_day", hour(col("timestamp"))) \
              .groupBy("hour_of_day") \
              .agg(avg("temperature").alias("avg_temp")) \
              .orderBy("hour_of_day")

df_hourly.show()
df_hourly.toPandas().to_csv("task3_output.csv", index=False)


# Task 4: Window Function - Rank Sensors by Avg Temp
sensor_avg_temp = df.groupBy("sensor_id").agg(avg("temperature").alias("avg_temp"))

windowSpec = Window.orderBy(col("avg_temp").desc())
ranked_sensors = sensor_avg_temp.withColumn("rank_temp", dense_rank().over(windowSpec))

top_5 = ranked_sensors.limit(5)
top_5.show()
top_5.toPandas().to_csv("task4_output.csv", index=False)


# Task 5: Pivot & Interpretation
df_with_hour = df.withColumn("hour_of_day", hour(col("timestamp")))

pivot_df = df_with_hour.groupBy("location").pivot("hour_of_day").agg(avg("temperature")).orderBy("location")
pivot_df.show()
pivot_df.toPandas().to_csv("task5_output.csv", index=False)

# Optional Summary/Insights (prints only)
max_temp_info = pivot_df.select([col for col in pivot_df.columns[1:]]) \
                        .summary("max")
print("Maximum average temperatures by hour across all locations:")
max_temp_info.show()
