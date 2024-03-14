#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
            user=argv[1], password=argv[2], database=argv[3], host="localhost", port=3306)

    cursor = connection.cursor()
    state_name = argv[4]
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC", (state_name,))
    result = cursor.fetchall()
    for x in result:
        print(x)
