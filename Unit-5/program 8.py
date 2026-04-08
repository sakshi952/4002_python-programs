#Names Starting with “N” and Length = 5
import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("SELECT * FROM student WHERE name LIKE 'N____'")
rows = cur.fetchall()

if rows:   # if list is not empty
    for row in rows:
        print(row)
else:
    print("No student found with name starting with 'N' and length = 5.")

conn.close()
