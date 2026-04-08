#histogram of student ages
import matplotlib.pyplot as plt

# Example list of ages (no '...')
ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
        28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
        38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
        48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
        58, 59, 60, 61, 62, 63, 64, 65, 66, 67]

# Define bins (age groups)
bins = [0, 10, 20, 30, 40, 50, 60, 120]

# Create histogram
plt.hist(ages, bins=bins, edgecolor='black')
plt.title("Age Distribution of Students")
plt.xlabel("Age Groups")
plt.ylabel("Number of Students")
plt.show()
