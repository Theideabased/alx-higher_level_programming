#!/usr/bin/env python3
import MySQLdb
import sys

# Check if an argument was provided
if len(sys.argv) < 2:
    print("Usage: python script_name.py argument")
    sys.exit(1)

# Get the argument from the command line
search_argument = sys.argv[1]

# Connect to the database
conn = MySQLdb.connect(host="localhost", user="root", passwd="root",\
        db="hbtn_0e_0_usa", charset="utf8", port=3306)
cur = conn.cursor()

# Execute the SQL query with the provided argument
query = "SELECT * FROM states WHERE name LIKE %s"
cur.execute(query, (search_argument + '%',))

# Fetch and print the results
query_row = cur.fetchall()
for row in query_row:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()

