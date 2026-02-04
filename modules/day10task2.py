import pandas as pd
import logging

logging.basicConfig(
    filename="entry.log",              # log file name
    level=logging.INFO,               # minimum log level
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def pandas_summary():
    try:
        df = pd.read_csv("phonebook.csv")
        logging.info(f"Contacts displayed")

        print("\n--- Phonebook Summary (Using Pandas) ---")
        print("Total contacts:", len(df))

        print("\nColumn Info:")
        df.info()

        print("\nFirst 5 Contacts:")
        print(df.head())

    except FileNotFoundError:
        print("phonebook.csv not found.")
    except pd.errors.EmptyDataError:
        print("phonebook.csv is empty.")



print("Hello Git World")



if __name__ == "__main__":
    pandas_summary()



