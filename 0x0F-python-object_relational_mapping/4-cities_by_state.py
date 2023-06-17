#!/usr/bin/python3
"""
takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument

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

        cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")

        result = cursor.fetchall()
        for row in result:
            print(row)

    except Exception:
        print("Failed to connect with databse")
        exit(0)

    cursor.close()
    db.close()
