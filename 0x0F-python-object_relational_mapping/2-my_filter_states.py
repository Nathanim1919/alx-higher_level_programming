#!/usr/bin/python3
"""
    ascript that takes an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches
    the argumet

"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    try:
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                username=sys.argv[1],
                passwd=sys.argv[2],
                database=db
                )
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC").format(sys.argv[4])

    except Exception:
        print("Failed to connect with databse")
        exit(0)

    cursor.close()
    db.close();
