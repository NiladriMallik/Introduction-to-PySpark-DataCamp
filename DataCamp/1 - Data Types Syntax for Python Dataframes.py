from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType

my_schema = StructType([
    StructField('id', IntegerType(), nullable = False),
    StructField('name', StringType(), nullable = True),
    StructField('scores', ArrayType(IntegerType()), nullable = True)
])

df = spark.createDataFrame(data, schema = my_schema)