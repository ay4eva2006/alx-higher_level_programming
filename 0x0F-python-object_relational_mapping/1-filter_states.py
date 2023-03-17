#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":

# MySQL database configuration
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

# Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

# Create a cursor object
    cur = db.cursor()

# Execute the SQL query to select states with name starting with 'N'
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC""")

# Fetch all the rows in a list
    rows = cur.fetchall()

# Print the results
    for row in rows:
        print(row)

# Close the cursor and database connection
    cur.close()
    db.close()
