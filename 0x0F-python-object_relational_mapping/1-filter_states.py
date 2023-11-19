#!/usr/bin/python3
"""
Databse access
"""

import MySQLdb
import sys

"""
Connect to db and execute
"""


def createconn(username, password, dbname, host="localhost", port=3306):
    """
    Creates a connection to a database
    Returns the connection object
    """
    return MySQLdb.connect(host=host, port=port, user=username,
                           passwd=password, db=dbname,
                           charset="utf8")


def runsql(script, conn):
    """
    Creates a cursor from a conn to the database and runs
    an sql script
    """
    cur = conn.cursor()
    cur.execute(script)
    result = cur.fetchall()
    cur.close()
    return result


def displayresults(results):
    """
    Print a list of arrays to stdout
    """
    for row in results:
        print(row)


if __name__ == "__main__":
    conn = createconn(sys.argv[1], sys.argv[2], sys.argv[3])
    script = "SELECT id, name "
    script = script + "FROM states "
    script = script + "WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
    results = runsql(script, conn)
    displayresults(results)
    conn.close()

