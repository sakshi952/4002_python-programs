# open the file in read mode
file = open("sample.txt", "r")

# read the content of the file
content = file.read()

# display file contents
print("File Content:\n")
print(content)

# count words
words = content.split()
word_count = len(words)

print("\nNumber of words in the file:", word_count)

# close the file
file.close()
