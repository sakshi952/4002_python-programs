#9 Valid Emails using Regular Expression
import pandas as pd
import re

# Load Excel file
df = pd.read_excel("students.xlsx")

# Regex for valid email
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$'

print("\nValid Email Records:")
for i, email in enumerate(df['E-Mail']):
    if re.match(pattern, str(email)):
        # Print neatly: RollNo, Name, Email
        print(f"RollNo: {df.iloc[i]['RollNo']}, Name: {df.iloc[i]['Name']}, Email: {email}")
