#display all records
import sqlite3
conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("SELECT * FROM student")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
