# Write a program to load above excel file and use dropna() and fillna() functions separately.
import pandas as pd
df = pd.read_excel("students.xlsx")

print("\nUsing dropna():")
print(df.dropna())

print("\nUsing fillna():")
print(df.fillna("Not Available"))
