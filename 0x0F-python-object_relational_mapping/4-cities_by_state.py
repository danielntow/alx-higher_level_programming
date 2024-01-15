#!/usr/bin/python3
"""List all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Assign command line arguments to variables
    username, password, database = sys.argv[1:]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database, charset="utf8")
        cur = db.cursor()

        # Execute SQL query to select all cities sorted by cities.id
        # Execute SQL query to select all cities sorted by cities.id
        cur.execute("""SELECT cities.id, cities.name, states.name
               FROM states
               JOIN cities
               ON states.id=cities.state_id""")

        # Fetch all rows at once
        query_rows = cur.fetchall()

        # Display results
        for row in query_rows:
            print("{}".format(row))

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'cur' in locals() and cur:
            cur.close()
        if 'db' in locals() and db:
            db.close()
