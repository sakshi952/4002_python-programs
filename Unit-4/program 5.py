# Write a program to enter the name of 5 companies and its employee size and display as bar graph.
import matplotlib.pyplot as plt
companies = ['TCS', 'Infosys', 'Wipro', 'HCL', 'Tech Mahindra']
employees = [45000, 38000, 32000, 29000, 27000]

plt.bar(companies, employees, color='skyblue')
plt.title("Company Employee Sizes")
plt.xlabel("Company")
plt.ylabel("Employees")
plt.show()
