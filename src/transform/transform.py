from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("JSONFileProcessing") \
    .getOrCreate()

# Replace 'path_to_json_file' with the actual path to your JSON file
json_file_path = ".../data.json"

# Read JSON file into a DataFrame
df = spark.read.json(json_file_path)

df.show()


spark.stop()

