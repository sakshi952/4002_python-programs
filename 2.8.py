# Program to copy contents of one text file to another

source = open("source.txt", "r")
destination = open("destination.txt", "w")

data = source.read()      # read content from source file
destination.write(data)   # write content into destination file

source.close()
destination.close()

print("File copied successfully.")
