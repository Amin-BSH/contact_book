from typing import Dict

from prettytable import SINGLE_BORDER, PrettyTable


class ContactBook:
    """In this ContactBook class you can add, delete, edit, view on contact, and view all contacts"""

    def __init__(self) -> None:
        self.contacts_dict: Dict = {}

    def add_contact(self, name: str, email: str, phone: str, address: str) -> None:
        """You can add contact with this method

        :param name: the name of the contact
        :param email: the email of the contact
        :param phone: the phone of the contact
        :param address: the address of the contact
        """
        if name not in self.contacts_dict:
            self.contacts_dict[name] = {
                "email": email,
                "phone": phone,
                "address": address,
            }
            print("-" * 20)
            print("Contact has been created successfully.")
            print("-" * 20)
        else:
            print("-" * 20)
            print(
                "A contact with this name already exists. Please choose another name."
            )
            print("-" * 20)

    def delete_contact(self, name: str) -> None:
        """You can delete a contact with this method

        :param name: The name of the contact that you want to delete.
        """
        if name in self.contacts_dict:
            del self.contacts_dict[name]
        else:
            print("-" * 20)
            print("Contact not found.")
            print("-" * 20)

    def edit_contact(self, name: str, email: str, phone: str, address: str) -> None:
        """You can edit a contact with using this method. You must enter the name of the contact that you want to edit.

        :param name: the name of the contact
        :param email: the email of the contact
        :param phone: the phone of the contact
        :param address: the address of the contact
        """
        if name in self.contacts_dict:
            if email or email == "":
                self.contacts_dict[name]["email"] = "" if email == "" else email
            if phone or phone == "":
                self.contacts_dict[name]["phone"] = "" if phone == "" else phone
            if address or address == "":
                self.contacts_dict[name]["address"] = "" if address == "" else address
            print("-" * 20)
            print("Contact has been edited successfully.")
        else:
            print("-" * 20)
            print("Contact not found.")
            print("-" * 20)

    def view_contacts(self):
        """You can see all the contact that you have with this method."""
        if self.contacts_dict:
            table = PrettyTable()
            table.align = "c"
            table.field_names = ["Name", "Email", "Phone", "Address"]
            table.set_style(SINGLE_BORDER)
            for key, value in self.contacts_dict.items():
                table.add_row([key, value["email"], value["phone"], value["address"]])

            print(table.get_string(sortby="Name", reversesort=True, border=True))

        else:
            print("-" * 20)
            print("No contacts found.")

    def view_contact(self, name: str) -> None:
        """You can view a specific contact with this method.

        :param name: name of the contact
        """
        if name in self.contacts_dict:
            table = PrettyTable()
            table.align = "c"
            table.field_names = ["Name", "Email", "Phone", "Address"]
            table.set_style(SINGLE_BORDER)
            table.add_row([name, self.contacts_dict[name]['email'], self.contacts_dict[name]['phone'], self.contacts_dict[name]['address']])

            print(table.get_string(sortby="Name", reversesort=True, border=True))
        else:
            print("-" * 20)
            print("Contact not found.")
            print("-" * 20)


if "__main__" == __name__:
    contact = ContactBook()

while True:
    print("\n--- Contact Book Application ---")
    print("Enter 1 to add a contact.")
    print("Enter 2 to delete a contact.")
    print("Enter 3 to edit a contact.")
    print("Enter 4 to view a contact.")
    print("Enter 5 to view all contacts.")
    print("Enter 6 to exit the program.")

    contact_choice = input("Please choose an option: ")

    if contact_choice == "1":
        name = input("Enter a name: ")
        email = input("Enter an email: ")
        phone = input("Enter a phone number: ")
        address = input("Enter an address: ")
        contact.add_contact(name=name, email=email, phone=phone, address=address)
    elif contact_choice == "2":
        name = input("Enter a name: ")
        contact.delete_contact(name=name)
    elif contact_choice == "3":
        name = input("Enter a name: ")
        email = input("Enter an email: ")
        phone = input("Enter a phone number: ")
        address = input("Enter an address: ")
        contact.edit_contact(name=name, email=email, phone=phone, address=address)
    elif contact_choice == "4":
        name = input("Enter a name: ")
        contact.view_contact(name=name)
    elif contact_choice == "5":
        contact.view_contacts()
    elif contact_choice == "6":
        print("-" * 20)
        print("\U0001F44B You have exited successfully")
        print("-" * 20)
        break
    else:
        print("\U0001F914 You entered an invalid command")
