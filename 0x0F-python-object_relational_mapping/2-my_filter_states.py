#!/usr/bin/python3
"""
Script displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # if len(sys.argv) != 5:
    #     print(
    #         "Usage: {} <username> <password> <database> <argument>".format(
    #             sys.argv[0]
    #         )
    #     )
    #     sys.exit(1)

    username, password, database, argument = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password,
        db=database
    )

    cur = db.cursor()
    # Execute query with parameterized query
    cur.execute(
        "SELECT * FROM states WHERE name IN (%s) ORDER BY id ASC", (argument,)
    )

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()
