class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number

    def edit_contact(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
        else:
            print("Contact not found.")

    def search_contact(self, name):
        if name in self.contacts:
            return f"Name: {name}, Phone Number: {self.contacts[name]}"
        else:
            return "Contact not found."

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found.")
