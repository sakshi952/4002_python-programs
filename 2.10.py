import zipfile

# Function to zip a file
def zip_file():
    file_name = input("Enter file name to zip: ")
    zip_name = "compressed.zip"

    with zipfile.ZipFile(zip_name, 'w') as z:
        z.write(file_name)

    print("File zipped successfully")


# Function to unzip a file
def unzip_file():
    zip_name = input("Enter zip file name: ")

    with zipfile.ZipFile(zip_name, 'r') as z:
        z.extractall()

    print("File unzipped successfully")


# Menu
while True:
    print("\n1. Zip File")
    print("2. Unzip File")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        zip_file()
    elif choice == "2":
        unzip_file()
    elif choice == "3":
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
