#!/usr/bin/python3
"""list all staes with a name starting with N"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '%N' ORDER BY id ASC";)
    rows = cur.fetchall()
    for row in rows:
        print(row)