#Create Table from List of Column Definitions
import sqlite3
columns = [
    ["name", "varchar", 20],
    ["qualification", "varchar", 20],
    ["post", "varchar", 20],
    ["salary", "int", 6]
]

table_sql = "CREATE TABLE IF NOT EXISTS employee ("
for col in columns:
    table_sql += f"{col[0]} {col[1]}({col[2]}), "
table_sql = table_sql.rstrip(", ") + ")"

conn = sqlite3.connect("students.db")
cur = conn.cursor()
cur.execute(table_sql)
conn.commit()
conn.close()
print("Employee table created.")
