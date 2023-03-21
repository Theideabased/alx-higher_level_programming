#!/usr/bin/python3

"""
filter table by what was inputed
importing the sqldb modules and
connecting the database with the 
username and password
"""

import SQLdb 
from sys import argv

if __name__ == '__main__':
    """
    Acess the database with the
    username, the password, the port and
    the database name
    """

    db = MySQLdb.connect(host= 'localhost', user = argv[1],
                         port =3306, passwd = argv[2], db = argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM \
                 WHERE name BINARY '{}'\
                 ORDER BY states.id ASC".format(argv[4]))
    row = cur.fetchall()

    for row in rows:
        print(row)

