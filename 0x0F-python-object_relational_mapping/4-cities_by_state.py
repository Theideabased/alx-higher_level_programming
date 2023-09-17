#!/usr/bin/python3
""" this code will print all in cities from the hbtn_0e_4_usa
database"""

# importing the important library
import MySQLdb

# connecting to mysql server
conn = MySQLdb.connect(port=3306, host='localhost', passwd='root', user='root',\
        db='hbtn_0e_4_usa', charset='utf8')
cur = conn.cursor()

# executing the SQL codes
cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
        LEFT OUTER JOIN states ON cities.state_id=states.id \
        ORDER BY cities.id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)

# closing my database connections
cur.close()
conn.close()
