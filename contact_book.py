contacts = []


def add_contact():

    print("\n===== ADD CONTACT =====")

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    print("Contact added successfully!")


def view_contacts():

    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n===== CONTACT LIST =====")

    for i, contact in enumerate(contacts, start=1):

        print(f"\nContact {i}")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Address:", contact["address"])


def search_contact():

    search = input("\nEnter name or phone to search: ").lower()

    found = False

    for contact in contacts:

        if (
            search in contact["name"].lower()
            or search in contact["phone"]
        ):

            print("\nContact Found!")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])

            found = True

    if not found:
        print("Contact not found.")


def update_contact():

    view_contacts()

    if not contacts:
        return

    try:
        number = int(input("\nEnter contact number to update: "))

        if 1 <= number <= len(contacts):

            contact = contacts[number - 1]

            print("\nPress Enter to keep old information.")

            name = input("New name: ")
            phone = input("New phone: ")
            email = input("New email: ")
            address = input("New address: ")

            if name:
                contact["name"] = name

            if phone:
                contact["phone"] = phone

            if email:
                contact["email"] = email

            if address:
                contact["address"] = address

            print("Contact updated successfully!")

        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_contact():

    view_contacts()

    if not contacts:
        return

    try:
        number = int(input("\nEnter contact number to delete: "))

        if 1 <= number <= len(contacts):

            deleted = contacts.pop(number - 1)

            print(
                "Deleted contact:",
                deleted["name"]
            )

        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n==========================")
    print("       CONTACT BOOK")
    print("==========================")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice!")
