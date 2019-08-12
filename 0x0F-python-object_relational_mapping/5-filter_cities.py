#!/usr/bin/python3
'''
a script that lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute('''SELECT cities.name FROM cities
                 JOIN states ON states.id = cities.state_id
                 WHERE states.name=%s''', (argv[4],))
    cities = cur.fetchall()

    for city in cities[:-1]:
        print(city[0], end=", ")
    last = cities[-1]
    print(last[0])

    cur.close()
    db.close()
