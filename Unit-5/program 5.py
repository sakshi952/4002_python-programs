#Update Student Detail
import sqlite3
roll = input("Enter Roll No to update: ")
new_city = input("Enter new city: ")

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("UPDATE student SET city = ? WHERE rollno = ?", (new_city, roll))
conn.commit()
conn.close()
print("Student updated.")
