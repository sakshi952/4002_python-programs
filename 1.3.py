# Input marks of 4 subjects
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))

# Calculate total and percentage
total = m1 + m2 + m3 + m4
percentage = (total / 400) * 100

# Display total and percentage
print("Total Marks =", total)
print("Percentage =", percentage)

# Determine grade
if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")
