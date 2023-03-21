#!/usr/bin/python3

"""
Display all the value in state table of the database
hbtn_0e_0_usa whose name matches the argument given
that is safe for sql injection
"""

import MySQLdb
from sys import argv

"""
Acess the database with the host,
port, database name, and passwd
"""
if __name__ == "__main__":
    db = MySQLdb.connect(user = argv[1], port = 3306,
                         host = 'localhost', passwd = argv[2],
                         db = argv[3], charset="utf8") 
    c = db.cursor()
    c.execute("SELECT * FROM state WHERE name LIKE %s ORDER BY id ASC",
            (argv[4]))
    row = cur.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
