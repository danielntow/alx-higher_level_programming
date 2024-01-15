#!/usr/bin/python3
"""List states with a name starting with N from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database, charset="utf8")
        cur = db.cursor()

        # execute query
        cur.execute("SELECT * FROM states WHERE \
    name LIKE 'N%' ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'cur' in locals() and cur:
            cur.close()
        if 'db' in locals() and db:
            db.close()
