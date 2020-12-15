from pyspark import SparkContext
from awsglue.context import GlueContext

# Spark Init
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
glueContext.setConf("spark.sql.shuffle.partitions", "2")

