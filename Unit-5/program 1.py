import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("SELECT * FROM student")
row = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

conn.close()
