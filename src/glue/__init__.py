from pyspark import SparkContext
from awsglue.context import GlueContext

# Spark Init
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)

# Change partitions from 200 to 2 for small data
glueContext.setConf("spark.sql.shuffle.partitions", "2")

