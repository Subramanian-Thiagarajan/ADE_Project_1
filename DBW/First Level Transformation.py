# Databricks notebook source
dbutils.fs.ls("/mnt/bronze/SalesLT/")

# COMMAND ----------

dbutils.fs.ls("/mnt/silver/")

# COMMAND ----------

address_table_path = "/mnt/bronze/SalesLT/Address/Address.parquet"
df = spark.read.format('parquet').load(address_table_path)

# COMMAND ----------

display(df)

# COMMAND ----------

df.show(5)

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType


# COMMAND ----------


df = df.withColumn("ModifiedDate", date_format(from_utc_timestamp(df["ModifiedDate"].cast(TimestampType()),"UTC"),"yyyy-MM-dd"))

# COMMAND ----------

display(df)

# COMMAND ----------

# Modify Date in all the tables
tableName = []

for i in dbutils.fs.ls('mnt/bronze/SalesLT/'):
    tableName.append(i.name.split('/')[0])

# COMMAND ----------

tableName

# COMMAND ----------

for i in tableName:
    path = '/mnt/bronze/SalesLT/' + i + '/' + i + '.parquet'
    df = spark.read.format('parquet').load(path)
    column = df.columns

    for c in column:
        if "date" in c or "Date" in c:
            df = df.withColumn(c, date_format(from_utc_timestamp(df[c].cast(TimestampType()),"UTC"),"yyyy-MM-dd"))
    
    output_path = '/mnt/silver/SalesLT/' + i + '/'
    df.write.format('delta').mode("overwrite").save(output_path)

# COMMAND ----------


