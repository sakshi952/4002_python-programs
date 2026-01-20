numbers = []

print("Enter 10 numbers:")
for i in range(10):
    num = int(input())
    numbers.append(num)

odd_numbers = [n for n in numbers if n % 2 != 0]

if odd_numbers:
    print("Largest odd number is:", max(odd_numbers))
else:
    print("No odd numbers entered")
