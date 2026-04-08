import pandas as pd

df = pd.read_excel("students.xlsx")  # Replace with your actual file name
print("Columns:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)
