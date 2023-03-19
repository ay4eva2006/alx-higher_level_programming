#!/usr/bin/python3
"""
This script retrieves data from the 'states' table in a safe way,
using the LIKE operator to match the state name, and removes the repetition.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Check if all arguments are present
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        exit(1)

    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query in a safe way and remove repetition
    cur.execute("SELECT DISTINCT * FROM states WHERE name LIKE %s", (state_name,))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()
