# Write a program to enter the profit of 5 years and display the profit as line graph. 
import matplotlib.pyplot as plt

years = ['2019', '2020', '2021', '2022', '2023']
profit = [12000, 15000, 18000, 21000, 25000]

plt.plot(years, profit, marker='o')
plt.title("Profit Over 5 Years")
plt.xlabel("Year")
plt.ylabel("Profit (₹)")
plt.grid(True)
plt.show()
