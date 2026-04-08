#Delete Student Record
import sqlite3
roll = input("Enter Roll No to delete: ")

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("DELETE FROM student WHERE rollno = ?", (roll,))
conn.commit()
conn.close()
print("Student deleted.")
