#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Take mysql username, password, database name, and state name as arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password, db=database_name, charset="utf8")

    # Create a cursor to execute queries
    cur = conn.cursor()

    # Use format to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(state_name)

    # Execute the query
    cur.execute(query)

    # Fetch all the results
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    conn.close()
