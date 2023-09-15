#!/usr/bin/env python3
""" this will print all the states that start
with N in the database hbtn_0e_0_usa"""

import MySQLdb
conn = MySQLdb.connect(user="root", passwd="root", host="localhost",\
        db="hbtn_0e_0_usa", charset="utf8", port=3306)
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
