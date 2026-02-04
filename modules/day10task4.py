import csv

phonebook = {}

def load_csv():
    try:
        with open("phonebook.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                phonebook[row["name"]] = row["phone"]
    except FileNotFoundError:
        save_to_csv()

def save_to_csv():
    with open("phonebook.csv", "w", newline="") as file:
        fieldnames = ["name", "phone"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for name, phone in phonebook.items():
            writer.writerow({"name": name, "phone": phone})

def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    phonebook[name] = number
    save_to_csv()
    print("Contact added & saved successfully!")

def search_contact():
    name = input("Enter name to search: ")
    if name in phonebook:
        print("Number:", phonebook[name])
    else:
        print("Contact not found")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        save_to_csv()
        print("Contact deleted & saved")
    else:
        print("Contact not found")

def view_all():
    for name, number in phonebook.items():
        print(name, ":", number)

def summary():
    print("Total contacts:", len(phonebook))

menu = {
    "1": add_contact,
    "2": search_contact,
    "3": delete_contact,
    "4": view_all,
    "5": summary
}

load_csv()

if __name__ == "__main__":
    while True:
        choice = input("Enter choice: ")
        func = menu.get(choice)
        if func:
            func()
