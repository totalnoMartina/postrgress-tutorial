import psycopg2

# Connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# Build a cursor object ofthe database
cursor = connection.cursor()

# Query 1 - Select all the records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the result (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

for result in results:
    print(result)