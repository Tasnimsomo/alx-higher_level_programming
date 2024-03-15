#!/usr/bin/python3
"""
This script  takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQL.db.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            database=argv[3])
    cursor = connection.cursor()
    state_name = argv[4]
    query = "SELECT * FROM cities WHERE state = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    for x in results:
        print(x)
