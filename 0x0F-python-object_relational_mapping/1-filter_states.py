import MySQLdb
from sys import argv

"""
Access to the database and get the states
from the database.
"""

if name == 'main':
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cursor = connection.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                    ORDER BY states.id ASC")
    results = cursor.fetchall()
    for x in results:
        print(x)
