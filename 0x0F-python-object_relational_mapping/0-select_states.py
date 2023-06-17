#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """


if __name__ == "__main__":

    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    #connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306,user=username, passwd=password, db=database)


    #Create a cursor object to interact with the database
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    #Fetch all the rows and display them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    #Close the cursor and databse conection
    cursor.close()
    db.close()
