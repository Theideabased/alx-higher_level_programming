#!/usr/bin/python3
"""  this will take and argument and print out
the table that resemble the argument"""

if __name__ == '__main__':
    # import the library
    import MySQLdb
    from sys import argv

    # connecting to mysql server
    conn = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                           db=argv[3], charset="utf8", port=3306)
    cur = conn.cursor()

    # executing my sql code
    cur.execute(f"SELECT * FROM states WHERE name LIKE BINARY '{argv[4]}'\
            ORDER BY states.id ASC")
    query_row = cur.fetchall()
    for row in query_row:
        print(row)

    # closing the connection with my server
    cur.close()
    conn.close()
