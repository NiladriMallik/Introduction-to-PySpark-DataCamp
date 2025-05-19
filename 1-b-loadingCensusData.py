# Read in the CSV
census_adult = spark.read.csv('adult_reduced.csv')

# Show the DataFrame
census_adult.show()