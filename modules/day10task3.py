"""
Docstring for day10task3
Recording what the program is doing (events, actions, errors, status messages) into a .txt or .log file instead of only showing them on the screen.
Debug errors

Track user actions

Monitor system behavior

Understand crashes after they happen
"""

import logging

# Configure logging
logging.basicConfig(
    filename="app.log",              # log file name
    level=logging.INFO,               # minimum log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def add_contact(name):
    logging.info(f"Contact added: {name}")
    print("Contact added successfully!")

def search_contact(name, phonebook):
    if name in phonebook:
        logging.info(f"Contact found: {name}")
        print("Number:", phonebook[name])
    else:
        logging.error(f"Contact not found: {name}")
        print("Contact not found")

# Example usage
phonebook = {"Gauri": "9876543210"}

add_contact("Aaryan")
search_contact("Gauri", phonebook)
search_contact("Rahul", phonebook)
