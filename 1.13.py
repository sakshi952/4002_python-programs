from functools import reduce

# Given list
numbers = [1, 2, 3, 4, 5, 6]

# map() → square of each number
squares = list(map(lambda x: x * x, numbers))
print("Squares using map():", squares)

# filter() → filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", even_numbers)

# reduce() → sum of all numbers
total = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce():", total)
