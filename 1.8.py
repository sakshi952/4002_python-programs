# Take string input
s = input("Enter a string: ")

# a) Count number of vowels
vowels = "aeiouAEIOU"
vowel_count = 0
for ch in s:
    if ch in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

# b) Count length of string (without using len())
length = 0
for ch in s:
    length += 1
print("Length of string:", length)

# c) Reverse the string
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)

# d) Find and replace operation
find_char = input("Enter character/string to find: ")
replace_char = input("Enter character/string to replace with: ")
new_string = s.replace(find_char, replace_char)
print("String after replace:", new_string)

# e) Check whether string is palindrome or not
if s == rev:
    print("The string is a Palindrome")
else:
    print("The string is NOT a Palindrome")
