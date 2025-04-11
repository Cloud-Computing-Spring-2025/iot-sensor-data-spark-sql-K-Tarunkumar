Here's an updated version of the `README.md` that includes detailed **Sample Input** and **Sample Output** for each specific task you may run in your Spark SQL analysis:

---

## 🚀 Running the Project

### Step 1: Prepare Your Environment

Ensure the following are in place:
- **Python 3.8+**
- **Java 8 or 11** (required by Spark)
- **Apache Spark 3.5.x**
- **pyspark** Python package installed (use `pip install pyspark`)

### Step 2: Set up and Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/iot-sensor-data-spark-sql.git
   cd iot-sensor-data-spark-sql
   ```
    1.1
    ### ✅ **1. Prerequisites Check**

Make sure you have the following installed:

#### a. Python
```bash
python3 --version
```

#### b. PySpark
```bash
pip install pyspark
```

#### c. Faker (if you're generating dummy data)
```bash
pip install faker
```

#### d. Apache Spark
To verify Spark:
```bash
spark-submit --version
```
2. **Add the `sensor_data.csv` file**  
   Place the `sensor_data.csv` file in the root of the project folder.

3. **Run the analysis**  
   Run the script using `spark-submit` or Python:
   ```bash
   spark-submit task.py
   ```

---

## 📂 Sample Input

The `sensor_data.csv` should look like this:

```csv
sensor_id,temperature,humidity,location,timestamp
S1,22.5,60,Room1,2025-04-11 10:00:00
S2,23.0,58,Room2,2025-04-11 10:05:00
S1,21.0,65,Room1,2025-04-11 10:10:00
S3,24.1,55,Room3,2025-04-11 10:15:00
S2,22.8,59,Room2,2025-04-11 10:20:00
```

---

## 📝 Tasks with Sample Input and Output

### **Task 1: Average Temperature per Location**

**Description:** Calculate the average temperature for each location.

**SQL Query in Spark:**

```python
df.createOrReplaceTempView("sensor_data")
avg_temp_per_location = spark.sql("""
    SELECT location, AVG(temperature) AS avg_temp
    FROM sensor_data
    GROUP BY location
""")
avg_temp_per_location.show()
```

**Sample Output:**

```text
+--------+-----------+
|location|avg_temp   |
+--------+-----------+
|Room1   |21.75      |
|Room2   |22.9       |
|Room3   |24.1       |
+--------+-----------+
```

---

### **Task 2: Sensor with Maximum Temperature**

**Description:** Find the sensor that recorded the highest temperature.

**SQL Query in Spark:**

```python
max_temp_sensor = spark.sql("""
    SELECT sensor_id, MAX(temperature) AS max_temp, location
    FROM sensor_data
    GROUP BY sensor_id, location
    ORDER BY max_temp DESC
    LIMIT 1
""")
max_temp_sensor.show()
```

**Sample Output:**

```text
+--------+-----------+--------+
|sensor_id|max_temp   |location|
+--------+-----------+--------+
|S3       |24.1       |Room3   |
+--------+-----------+--------+
```

---

### **Task 3: Total Humidity by Location**

**Description:** Calculate the total humidity for each location.

**SQL Query in Spark:**

```python
total_humidity_per_location = spark.sql("""
    SELECT location, SUM(humidity) AS total_humidity
    FROM sensor_data
    GROUP BY location
""")
total_humidity_per_location.show()
```

**Sample Output:**

```text
+--------+-------------+
|location|total_humidity|
+--------+-------------+
|Room1   |125         |
|Room2   |117         |
|Room3   |55          |
+--------+-------------+
```

---

### **Task 4: Sensors Recorded in the Last Hour**

**Description:** List all sensors that recorded data in the last hour based on the timestamp.

**SQL Query in Spark:**

```python
from pyspark.sql.functions import current_timestamp

df_with_timestamp = df.withColumn("timestamp", df["timestamp"].cast("timestamp"))
df_with_timestamp.createOrReplaceTempView("sensor_data")

recent_sensors = spark.sql("""
    SELECT sensor_id, temperature, location, timestamp
    FROM sensor_data
    WHERE timestamp >= current_timestamp() - INTERVAL 1 HOUR
""")
recent_sensors.show()
```

**Sample Output:**

```text
+--------+-----------+--------+-------------------+
|sensor_id|temperature|location|timestamp          |
+--------+-----------+--------+-------------------+
|S2       |22.8       |Room2   |2025-04-11 10:20:00 |
|S1       |21.0       |Room1   |2025-04-11 10:10:00 |
+--------+-----------+--------+-------------------+
```

---

### **Task 5: Sensor Readings by Hour**

**Description:** Get the count of sensor readings per hour.

**SQL Query in Spark:**

```python
df_with_hour = df.withColumn("hour", hour(df["timestamp"]))
df_with_hour.createOrReplaceTempView("sensor_data")

sensor_readings_by_hour = spark.sql("""
    SELECT hour, COUNT(*) AS readings_count
    FROM sensor_data
    GROUP BY hour
""")
sensor_readings_by_hour.show()
```

**Sample Output:**

```text
+----+-------------+
|hour|readings_count|
+----+-------------+
|10  |5            |
+----+-------------+
```

---

## 🚀 Output Overview

Each task produces a DataFrame that is displayed in the console. The output format is tabular with column headers representing the computed data.

Let me know if you'd like further clarifications or more tasks added!Here's an updated version of the `README.md` that includes detailed **Sample Input** and **Sample Output** for each specific task you may run in your Spark SQL analysis:

---

## 🚀 Running the Project

### Step 1: Prepare Your Environment

Ensure the following are in place:
- **Python 3.8+**
- **Java 8 or 11** (required by Spark)
- **Apache Spark 3.5.x**
- **pyspark** Python package installed (use `pip install pyspark`)

### Step 2: Set up and Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/iot-sensor-data-spark-sql.git
   cd iot-sensor-data-spark-sql
   ```

2. **Add the `sensor_data.csv` file**  
   Place the `sensor_data.csv` file in the root of the project folder.

3. **Run the analysis**  
   Run the script using `spark-submit` or Python:
   ```bash
   spark-submit task.py
   ```

---

## 📂 Sample Input

The `sensor_data.csv` should look like this:

```csv
sensor_id,temperature,humidity,location,timestamp
S1,22.5,60,Room1,2025-04-11 10:00:00
S2,23.0,58,Room2,2025-04-11 10:05:00
S1,21.0,65,Room1,2025-04-11 10:10:00
S3,24.1,55,Room3,2025-04-11 10:15:00
S2,22.8,59,Room2,2025-04-11 10:20:00
```

---

## 📝 Tasks with Sample Input and Output

### **Task 1: Average Temperature per Location**

**Description:** Calculate the average temperature for each location.

**SQL Query in Spark:**

```python
df.createOrReplaceTempView("sensor_data")
avg_temp_per_location = spark.sql("""
    SELECT location, AVG(temperature) AS avg_temp
    FROM sensor_data
    GROUP BY location
""")
avg_temp_per_location.show()
```

**Sample Output:**

```text
+--------+-----------+
|location|avg_temp   |
+--------+-----------+
|Room1   |21.75      |
|Room2   |22.9       |
|Room3   |24.1       |
+--------+-----------+
```

---

### **Task 2: Sensor with Maximum Temperature**

**Description:** Find the sensor that recorded the highest temperature.

**SQL Query in Spark:**

```python
max_temp_sensor = spark.sql("""
    SELECT sensor_id, MAX(temperature) AS max_temp, location
    FROM sensor_data
    GROUP BY sensor_id, location
    ORDER BY max_temp DESC
    LIMIT 1
""")
max_temp_sensor.show()
```

**Sample Output:**

```text
+--------+-----------+--------+
|sensor_id|max_temp   |location|
+--------+-----------+--------+
|S3       |24.1       |Room3   |
+--------+-----------+--------+
```

---

### **Task 3: Total Humidity by Location**

**Description:** Calculate the total humidity for each location.

**SQL Query in Spark:**

```python
total_humidity_per_location = spark.sql("""
    SELECT location, SUM(humidity) AS total_humidity
    FROM sensor_data
    GROUP BY location
""")
total_humidity_per_location.show()
```

**Sample Output:**

```text
+--------+-------------+
|location|total_humidity|
+--------+-------------+
|Room1   |125         |
|Room2   |117         |
|Room3   |55          |
+--------+-------------+
```

---

### **Task 4: Sensors Recorded in the Last Hour**

**Description:** List all sensors that recorded data in the last hour based on the timestamp.

**SQL Query in Spark:**

```python
from pyspark.sql.functions import current_timestamp

df_with_timestamp = df.withColumn("timestamp", df["timestamp"].cast("timestamp"))
df_with_timestamp.createOrReplaceTempView("sensor_data")

recent_sensors = spark.sql("""
    SELECT sensor_id, temperature, location, timestamp
    FROM sensor_data
    WHERE timestamp >= current_timestamp() - INTERVAL 1 HOUR
""")
recent_sensors.show()
```

**Sample Output:**

```text
+--------+-----------+--------+-------------------+
|sensor_id|temperature|location|timestamp          |
+--------+-----------+--------+-------------------+
|S2       |22.8       |Room2   |2025-04-11 10:20:00 |
|S1       |21.0       |Room1   |2025-04-11 10:10:00 |
+--------+-----------+--------+-------------------+
```

---

### **Task 5: Sensor Readings by Hour**

**Description:** Get the count of sensor readings per hour.

**SQL Query in Spark:**

```python
df_with_hour = df.withColumn("hour", hour(df["timestamp"]))
df_with_hour.createOrReplaceTempView("sensor_data")

sensor_readings_by_hour = spark.sql("""
    SELECT hour, COUNT(*) AS readings_count
    FROM sensor_data
    GROUP BY hour
""")
sensor_readings_by_hour.show()
```

**Sample Output:**

```text
+----+-------------+
|hour|readings_count|
+----+-------------+
|10  |5            |
+----+-------------+
```

---
