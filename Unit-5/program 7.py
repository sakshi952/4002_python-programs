#Display Records with Valid Email (Regex)
import sqlite3
import re
conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("SELECT * FROM student")
rows = cur.fetchall()

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$'
print("Valid Emails:")
for row in rows:
    if re.match(pattern, row[4]):
        print(row)

conn.close()
