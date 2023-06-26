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


if __name__ == "__main__":
    conn = createconn(sys.argv[1], sys.argv[2], sys.argv[3])
    script = """
                SELECT cities.name
                FROM cities LEFT JOIN states ON
                cities.state_id = states.id
                WHERE states.name = '{}'
                ORDER BY cities.id ASC;
            """
    j = sys.argv[4]
    if ';' in j:
        j = j.split(';')[0][:-1]
    script = script.format(j)
    results = runsql(script, conn)
    print(", ".join([i[0] for i in results]))
    conn.close()
