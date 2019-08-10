#!/usr/bin/python3
'''
a script that lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute('''SELECT cities.id, cities.name, states.id FROM cities
                 JOIN states ON states.id = cities.state_id
                 ORDER BY cities.id ASC''')
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
