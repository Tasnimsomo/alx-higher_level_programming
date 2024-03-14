#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
            user=argv[1],
            password=argv[2],
            database=argv[3],
            host="localhost",
            port=3306
            )
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT * from states WHERE name LIKE 'N%' ORDER BY states.id ASC LIMIT 2")
    results = cursor.fetchall()
    for x in results:
        print(x)
