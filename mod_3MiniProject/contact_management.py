import re
contacts = {}

def add_contact():
    """
    This function allows users to add contact information, and checks to make sure the information is valid.
    """
    while True:
        new_contact_prompt = input("Would you like to add a new contact? ")
        if new_contact_prompt.lower() == "no":
            break
        elif new_contact_prompt.lower() == "yes":

            contact_name = input("Add contact name: ")
            phone_number = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            additional_info = input("Enter additional info (enter 'none' if there is nothing else to add): ")

            if not re.match(r"^\d{10}$", phone_number):
                print("Invalid phone number. Please enter a 10-digit number.")
                return
            if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                print("Invalid email address. Please enter a valid email.")
                return
            
            contacts[phone_number] = {
            "name": contact_name,
            "email": email,
            "additional_info": additional_info
            }
            print("Contact added successfully!")
        else:
            print("Please enter a valid response.")

def edit_contact():
    """
    This function allows you to select a contact using a phone number key, and decide whether and what
    you want to edit. Uses a while loop to make selections.
    """
    phone_number = input("Enter phone number of the contact to edit: ")
    if phone_number not in contacts:
        print("Contact not found.")
    else:
        print("Current contact information:")
        print("Name:", contacts[phone_number]["name"])
        print("Email:", contacts[phone_number]["email"])
        print("Additional Info:", contacts[phone_number]["additional_info"])

    while True:
        print("Which field would you like to edit?")  
        print("1. Name")  
        print("2. Email")  
        print("3. Additional Info")  
        print("4. Cancel")

        user_choice = input("Choose a number to select a menu option: ")

        if user_choice == "1":
            new_name = input("Enter new name for your contact: ")
            if new_name == "back":
                print("Nothing has been changed.")
            elif new_name:
                contacts[phone_number]["name"] = new_name
                print(f"Name has been changed to {new_name}")

        if user_choice == "2":
            new_email = input("Enter a new email address for your contact: ")
            if new_email == "back":
                print("Nothing has been changed.")
            elif new_email:
                contacts[phone_number]["email"] == new_email
                print(f"Email has been changed to {new_email}")

        if user_choice == "3":
            new_info = input("Enter additional info to replace old info: ")
            if new_info == "back":
                print("Nothing has been changed.")
            elif new_info:
                contacts[phone_number]["email"] == new_info
                print(f"Email has been changed to {new_info}")

        if user_choice == "4":
            print("All done with editing this contact!")
            break

def delete_contact():
    """
    This function allows users to delete contacts stored in the contacts dictionary.
    """
    phone_number = input("Enter the phone number of the contact you want to delete: ")
    if phone_number not in contacts:
        print("Contact not found.")
    else:
        del contacts[phone_number]
        print("Contact deleted successfully.")

def search_contact():
    """
    This function allows users to search for individual contacts within the dictionary.
    """
    phone_number = input("Enter phone number of the contact to search: ")  
    if phone_number not in contacts:  
        print("Contact not found.")
    else:
        print("Name:", contacts[phone_number]["name"])  
        print("Email:", contacts[phone_number]["email"])  
        print("Additional Info:", contacts[phone_number]["additional_info"])

def display_contacts():
    """
    This function displays all contacts within the dictionary in a formatted way.
    """
    if not contacts:
        print("No contacts found.")
    else:
        for phone_number, contact in contacts.items():
            print("\n")
            print("Phone number:", phone_number)
            print("Name:", contact["name"])
            print("Email:", contact["email"])
            print("Additional Info:", contact["additional_info"])
            
def export_contacts():
    """
    This function exports contents of the contacts dictionary into a text file to display neatly.
    """
    with open("contacts.txt", "w") as file:  
        for phone_number, contact in contacts.items():  
            file.write(f"Phone Number: {phone_number}\n")
            file.write(f"Name: {contact['name']}\n")
            file.write(f"Email: {contact['email']}\n")
            file.write(f"Additional Info: {contact['additional_info']}\n")
            file.write("\n")
    print("Contacts exported to contacts.txt successfully!")

def menu():
    """
    This function allows users to make selections on what
    they would like to do regarding their contact book.
    """
    while True:  
        print("\n")
        print("Menu:")
        print("1. Add new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Quit")

        user_choice = input("Please enter a number indicating your menu selection: ")

        if user_choice == "1":
            add_contact()
        elif user_choice == "2":
            edit_contact()
        elif user_choice == "3":
            delete_contact()
        elif user_choice == "4":
            search_contact()
        elif user_choice == "5":
            display_contacts()
        elif user_choice == "6":
            export_contacts
        elif user_choice == "7":
            print("Goodbye!")
            break
        else:
            print("That is not a valid menu option. Please try again.")

menu()