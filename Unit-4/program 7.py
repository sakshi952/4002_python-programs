import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("students.xlsx")
gender_counts = df['Gender'].value_counts()

plt.bar(gender_counts.index, gender_counts.values, color=['blue', 'pink'])
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.show()
