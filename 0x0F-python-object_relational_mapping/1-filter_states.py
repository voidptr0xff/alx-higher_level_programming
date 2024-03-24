#!/usr/bin/python3
"""Filters to list states starting with 'N'"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
