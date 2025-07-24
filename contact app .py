# Contact Book Mini Project

# Data structures
contacts = {}  # Name: (phone, email)
action_history = set()  # Unique actions
menu_options = [
    "Add contact",
    "View all contacts", #this list is used to diaplay menu bar to users 
    "Search contact",
    "Delete contact",
    "View action history",
    "Exit"
]

def add_contact():
    name = input("Enter name: ").strip() # " mohan " -> "mohan"
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = (phone, email)  # Using tuple for contact info
    print(f"Contact '{name}' added.")
    action_history.add("added " + name)

def view_contacts():
    if not contacts:
        print("No contacts found.")
    for name, (phone, email) in contacts.items():
        print(f"Name: {name}, Phone: {phone}, Email: {email}")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        phone, email = contacts[name]
        print(f"Name: {name}, Phone: {phone}, Email: {email}")
    else:
        print("Contact not found.")
    action_history.add("searched " + name)

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
        action_history.add("deleted " + name)
    else:
        print("Contact not found.")

def view_history():
    print("Action History:")
    for action in action_history:
        print(action)

while True:
    print("\n--- Contact Book Menu ---")
    for idx, option in enumerate(menu_options, 1):
        print(f"{idx}. {option}")
    choice = input("Choose an option (1-6): ").strip()
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        view_history()
    elif choice == "6":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid option. Please choose 1-6.")