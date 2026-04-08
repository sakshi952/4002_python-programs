# Mobile Numbers with Country Code
import pandas as pd
import re

# Load Excel file
df = pd.read_excel("students.xlsx")

# Regex for country code format (e.g., 91-9999933333)
pattern = r'^\d{2}-\d{10}$'

print("\nMobile Numbers with Country Code:")
for i, mobile in enumerate(df['Mobile']):
    if re.match(pattern, str(mobile)):
        print(df.iloc[i])
