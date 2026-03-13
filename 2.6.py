file = open("numbers.txt", "w")

#data = file.read()

numbers = data.split()

if len(numbers) == 0:
    print("File is empty. No numbers found.")
else:
    numbers = list(map(int, numbers))

    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print("Numbers:", numbers)
    print("Total:", total)
    print("Maximum:", maximum)
    print("Minimum:", minimum)

file.close()
