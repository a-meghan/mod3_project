This is a project that manages contents in a contact book.
* = more detailed information provided.

The add_contact() function allows users to add contact information, and checks to make sure the information is valid.
* This function works by asking user questions and storing their responses in the correct places.
* It uses the re module to check response patterns to validate responses.

The edit_contact() function allows users to select a contact using a phone number key, and decide whether and what
    you want to edit. Uses a while loop to make selections.
* This function allows users to edt contacts based on the phone number associate with the contact- AKA the key to the contact values.

The delete_contact() function allows users to delete contacts stored in the contacts dictionary.
* This function will delete the contact of the phone number a user enters IF said contact exists within contact book.

The search_contact() function allows users to search for individual contacts within the dictionary.
* Searches a contact based on the phone number entered as user input.

The display_contact() function displays all contacts within the dictionary in a formatted way.

The export_contacts() function exports contents of the contacts dictionary into a text file to display neatly.

Finally we have the menu() function, which prompts users to choose an option and subsequently calls one of the above mentioned functions as
    selected.
