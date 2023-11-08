# Databricks notebook source
dbutils.fs.ls("/mnt/silver/SalesLT")

# COMMAND ----------

dbutils.fs.ls("/mnt/gold/")

# COMMAND ----------

address_table_path = "/mnt/silver/SalesLT/Address/"
df = spark.read.format('delta').load(address_table_path)

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace

col = df.columns

for old_col_name in col:
    new_col_name = "".join(["_" + char if char.isupper() and not old_col_name[i-1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")

    df = df.withColumnRenamed(old_col_name, new_col_name)

# COMMAND ----------

# Modify Date in all the tables
tableName = []

for i in dbutils.fs.ls('mnt/silver/SalesLT/'):
    tableName.append(i.name.split('/')[0])

# COMMAND ----------

for table in tableName:
    path = "/mnt/silver/SalesLT/" + table + '/'
    df = spark.read.format('delta').load(address_table_path)

    col = df.columns
    for old_col_name in col:
        new_col_name = "".join(["_" + char if char.isupper() and not old_col_name[i-1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")
        
        df = df.withColumnRenamed(old_col_name, new_col_name)

    output_path = "/mnt/gold/SalesLT/" + table + '/'
    df.write.format('delta').mode('overwrite').save(output_path)

# COMMAND ----------

display(df)

# COMMAND ----------


