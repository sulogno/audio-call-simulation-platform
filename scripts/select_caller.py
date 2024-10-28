import json

def load_contacts():
    try:
        with open('contacts/contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Contacts file not found. Please ensure 'contacts.json' exists in the 'contacts' folder.")
        return []

def select_caller_id():
    contacts = load_contacts()
    if not contacts:
        print("No contacts available to select.")
        return None
    
    print("Select a Caller ID from the following contacts:")
    for contact in contacts:
        print(f"{contact['id']}: {contact['name']} ({contact['phone']})")
    
    try:
        choice = int(input("Enter the contact ID to select as Caller ID: "))
        selected_contact = next((contact for contact in contacts if contact["id"] == choice), None)
    except ValueError:
        print("Invalid input. Please enter a numeric contact ID.")
        return None

    if selected_contact:
        print(f"Selected Caller ID: {selected_contact['name']} ({selected_contact['phone']})")
        return selected_contact
    else:
        print("Invalid contact ID.")
        return None

if __name__ == "__main__":
    select_caller_id()
