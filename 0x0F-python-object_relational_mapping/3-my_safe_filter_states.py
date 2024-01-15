#!/usr/bin/python3
"""Display all values in the states table
where name matches the argument (safe from MySQL injection)"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password>\
            <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Assign command line arguments to variables
    username, password, database, state_name = sys.argv[1:]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database, charset="utf8")
        cur = db.cursor()

        # Prepare SQL query with user input using parameterized query
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        # Execute SQL query with parameter
        cur.execute(query, (state_name,))
        query_rows = cur.fetchall()

        # Display results
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
