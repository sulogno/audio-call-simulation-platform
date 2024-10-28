import json
import time
from select_caller import select_caller_id

def initiate_call(contact):
    if contact:
        print(f"Initiating call to {contact['name']} ({contact['phone']})...")
        time.sleep(2)  # Simulate call connection time
        print("Call initiated successfully.")
    else:
        print("No contact selected. Unable to initiate call.")

if __name__ == "__main__":
    print("Starting automated call initiation process...")
    selected_contact = select_caller_id()
    initiate_call(selected_contact)
