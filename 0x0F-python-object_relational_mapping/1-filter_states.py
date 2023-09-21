#!/usr/bin/python3
""" this will print all the states that start
with N in the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], host="localhost",
                           db=argv[3], charset="utf8", port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
