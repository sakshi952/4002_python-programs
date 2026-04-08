#Search for a Particular Student
import sqlite3
roll = input("Enter Roll No to search: ")

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("SELECT * FROM student WHERE rollno = ?", (roll,))
row = cur.fetchone()

if row:
    print("Student Found:", row)
else:
    print("Student not found.")

conn.close()
