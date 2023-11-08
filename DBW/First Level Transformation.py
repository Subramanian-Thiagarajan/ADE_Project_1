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


