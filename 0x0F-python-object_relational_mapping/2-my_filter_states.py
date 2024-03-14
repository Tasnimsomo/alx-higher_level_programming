#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
            user=argv[1], password=argv[2], database=argv[3], host="localhost", port=3306)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC LIMIT 1".format(argv[4]))

    result = cursor.fetchall()
    for x in result:
        print(x)
