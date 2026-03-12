# Contact Book Application using Python Fundamentals

FILE_NAME = "contacts.txt"

# ---------- Function to Add Contact ----------
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    # open file in append mode
    file = open(FILE_NAME, "a")
    file.write(name + "," + phone + "," + email + "\n")
    file.close()

    print("Contact saved successfully!\n")


# ---------- Function to View Contacts ----------
def view_contacts():
    try:
        file = open(FILE_NAME, "r")
        data = file.readlines()
        file.close()

        if len(data) == 0:
            print("No contacts found.\n")
            return

        print("\n--- Contact List ---")
        for line in data:
            name, phone, email = line.strip().split(",")
            print("Name:", name)
            print("Phone:", phone)
            print("Email:", email)
            print("-------------------")

    except FileNotFoundError:
        print("No contacts file found.\n")


# ---------- Function to Search Contact ----------
def search_contact():
    search_name = input("Enter name to search: ")

    try:
        file = open(FILE_NAME, "r")
        found = False

        for line in file:
            name, phone, email = line.strip().split(",")
            if name.lower() == search_name.lower():
                print("\nContact Found:")
                print("Name:", name)
                print("Phone:", phone)
                print("Email:", email)
                found = True
                break

        file.close()

        if not found:
            print("Contact not found.\n")

    except FileNotFoundError:
        print("No contacts file found.\n")


#---------- Main Menu Loop ----------
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
         print("Invalid choice. Try again.\n")

