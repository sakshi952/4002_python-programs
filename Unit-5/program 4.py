#Insert Student Details
import sqlite3

data = (
    input("Roll No: "),
    input("Name: "),
    input("Gender: "),
    int(input("Age: ")),
    input("Email: "),
    input("Mobile: "),
    input("City: ")
)

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?)", data)
conn.commit()
conn.close()
print("Student inserted successfully.")
