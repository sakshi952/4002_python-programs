# Write a program to load above excel file and display following information
# List of students from Rajkot City
# List of Male students
# List of Male students from Rajkot City
#List of students whose age >= 20 
import pandas as pd
df = pd.read_excel("students.xlsx")

print("\nStudents from Rajkot:")
print(df[df['City'] == 'Rajkot'])

print("\nMale Students:")
print(df[df['Gender'] == 'Male'])

print("\nMale Students from Rajkot:")
print(df[(df['Gender'] == 'Male') & (df['City'] == 'Rajkot')])

print("\nStudents aged 20 or above:")
print(df[df['Age'] >= 20])
