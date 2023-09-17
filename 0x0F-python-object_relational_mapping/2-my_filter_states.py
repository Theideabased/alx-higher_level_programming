#!/usr/bin/python3
"""  this will take and argument and print out
the table that resemble the argument"""

# import the library
import MySQLdb
import sys

# connecting to mysql server
conn = MySQLdb.connect(host="localhost", user="root", passwd="root",\
        db="hbtn_0e_0_usa", charset="utf8", port=3306)
cur = conn.cursor()

# executing my sql code
cur.execute("SELECT * FROM states WHERE name = %s", (sys.argv,))
query_row = cur.fetchall()
for row in query_row:
    print(row)

# closing the connection with my server
cur.close()
conn.close()

