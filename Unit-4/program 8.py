#8 Course & Students → Pie Graph
import matplotlib.pyplot as plt

# Enter courses and student counts
courses = []
students = []

n = int(input("Enter number of courses: "))
for i in range(n):
    cname = input(f"Enter course {i+1} name: ")
    cstudents = int(input(f"Enter number of students in {cname}: "))
    courses.append(cname)
    students.append(cstudents)

# Find course with maximum students
max_index = students.index(max(students))

# Highlight the maximum slice
explode = [0] * n
explode[max_index] = 0.1  # separate the largest slice

# Plot pie chart
plt.pie(students, labels=courses, autopct='%1.1f%%', explode=explode, shadow=True)
plt.title("Students per Course")
plt.show()
