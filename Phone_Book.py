def add_contact(phone_book, name, number):
    phone_book[name] = number
    print(f"Contact '{name}' added with number '{number}'.")


def search_contact(phone_book, name):
    if name in phone_book:
        print(f"Contact '{name}' found with number '{phone_book[name]}'.")
    else:
        print(f"Contact '{name}' not found in the phone book.")


def delete_contact(phone_book, name):
    if name in phone_book:
        del phone_book[name]
        print(f"Contact '{name}' deleted from the phone book.")
    else:
        print(f"Contact '{name}' not found in the phone book.")


def display_contacts(phone_book):
    print("Contacts in the phone book:")
    for name, number in phone_book.items():
        print(f"{name}: {number}")


def main():
    phone_book = {}

    while True:
        print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter number: ")
            add_contact(phone_book, name, number)
        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(phone_book, name)
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(phone_book, name)
        elif choice == '4':
            display_contacts(phone_book)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
