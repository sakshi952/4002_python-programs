filename = "std.txt"

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    m1 = input("Enter Mark1: ")
    m2 = input("Enter Mark2: ")
    m3 = input("Enter Mark3: ")
    m4 = input("Enter Mark4: ")

    with open(filename, "a") as f:
        f.write(roll + "," + name + "," + m1 + "," + m2 + "," + m3 + "," + m4 + "\n")

    print("Student added successfully\n")


def search_student():
    roll = input("Enter Roll No to search: ")
    found = False

    with open(filename, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == roll:
                print("Record Found:", data)
                found = True

    if not found:
        print("Student not found\n")


def list_students():
    print("\nAll Students:")
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())
    print()


def update_student():
    roll = input("Enter Roll No to update: ")
    lines = []
    found = False

    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            data = line.strip().split(",")

            if data[0] == roll:
                print("Enter new details")
                name = input("Name: ")
                m1 = input("Mark1: ")
                m2 = input("Mark2: ")
                m3 = input("Mark3: ")
                m4 = input("Mark4: ")

                f.write(roll + "," + name + "," + m1 + "," + m2 + "," + m3 + "," + m4 + "\n")
                found = True
            else:
                f.write(line)

    if found:
        print("Student updated successfully\n")
    else:
        print("Student not found\n")


def delete_student():
    roll = input("Enter Roll No to delete: ")
    lines = []
    found = False

    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            data = line.strip().split(",")

            if data[0] != roll:
                f.write(line)
            else:
                found = True

    if found:
        print("Student deleted successfully\n")
    else:
        print("Student not found\n")


# Menu Driven Program
while True:
    print("----- Student Menu -----")
    print("1. Add Student")
    print("2. Search Student")
    print("3. List All Students")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        list_students()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice\n")
