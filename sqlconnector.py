import os
import mysql.connector

# Retrieve database credentials from environment variables
host = os.environ.get("DB_HOST")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
database = os.environ.get("DB_DATABASE")

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a simple SELECT query
cursor.execute("SELECT * FROM your_table")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Execute an INSERT query
data = ("John", "Doe", 25)
cursor.execute("INSERT INTO your_table (first_name, last_name, age) VALUES (%s, %s, %s)", data)
conn.commit()  # Commit the transaction

# Close the cursor and the connection
cursor.close()
conn.close()