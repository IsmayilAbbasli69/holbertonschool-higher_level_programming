#!/usr/bin/python3
<<<<<<< HEAD
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
=======
"""
Start the project
"""
import MySQLdb
import sys


if __name__ == "__main__":

    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

>>>>>>> 07d67ae256db1a77f4dabf4df8a3c79b9797aaea

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
<<<<<<< HEAD
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
=======
        user=user_name,
        passwd=password,
        db=db_name
    )


    cursor = db.cursor()


    cursor.execute("SELECT * FROM states ORDER BY id ASC")


    rows = cursor.fetchall()


    for row in rows:
        print(row)

    cursor.close()
    db.close()
>>>>>>> 07d67ae256db1a77f4dabf4df8a3c79b9797aaea
