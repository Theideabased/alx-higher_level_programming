#!/usr/bin/env python3
""" this code will print all in cities from the hbtn_0e_4_usa
database"""

# importing the important library
import MySQLdb
import sys

# making sure that only one argument is given
if len(sys.argv) > 2:
    print("Usage: python3 filename.py Argument")
    sys.exit(1)

# connecting to mysql server
conn = MySQLdb.connect(port=3306, host='localhost', passwd='root', user='root',\
        db='hbtn_0e_4_usa', charset='utf8')
cur = conn.cursor()

# executing the SQL codes
cur.execute("SELECT cities.name FROM cities LEFT OUTER JOIN states \
       ON cities.state_id=states.id WHERE states.name=%s",\
        (sys.argv[1],))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)

# closing my database connections
cur.close()
conn.close()
