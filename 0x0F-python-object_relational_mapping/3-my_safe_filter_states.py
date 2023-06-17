#!/usr/bin/python3
""" a script that takes in arguments and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
     script should take 4 arguments: mysql username, mysql password, database name
     and state name searched (safe from MySQL injection)
"""
if __name__ == '__main__':

    import sys
    import MySQLdb

    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3]
                )
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY states.id ASC", (sys.argv[4],))

        result = cursor.fetchall()
        for row in result:
            print(row)
    
    except Exception:
        print("Failed to connect with database")
        exit(0)
