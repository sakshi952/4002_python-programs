my_list = []

while True:
    print("\n--- LIST OPERATIONS MENU ---")
    print("1. Create List")
    print("2. Insert Element")
    print("3. Delete Element")
    print("4. Display List")
    print("5. Search Element")
    print("6. Sort List")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        my_list = []
        n = int(input("Enter number of elements: "))
        for i in range(n):
            value = int(input(f"Enter element {i+1}: "))
            my_list.append(value)
        print("List created successfully.")

    elif choice == 2:
        value = int(input("Enter element to insert: "))
        my_list.append(value)
        print("Element inserted.")

    elif choice == 3:
        value = int(input("Enter element to delete: "))
        if value in my_list:
            my_list.remove(value)
            print("Element deleted.")
        else:
            print("Element not found.")

    elif choice == 4:
        print("Current List:", my_list)

    elif choice == 5:
        value = int(input("Enter element to search: "))
        if value in my_list:
            print("Element found at index", my_list.index(value))
        else:
            print("Element not found.")

    elif choice == 6:
        my_list.sort()
        print("List sorted:", my_list)

    elif choice == 7:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
