import os
import sys
import sqlite3
from util.prompt import prompt_enter

def open_db(db_file: str):
    """Try opening an existing SQLite DB, return conn or None."""
    try:
        conn = sqlite3.connect(f"file:{db_file}?mode=rw", uri=True)
        print(f"Connected to '{db_file}'")
        prompt_enter(to="continue")
        return conn
    except sqlite3.OperationalError as e:
        print(f"Error opening '{db_file}': {e}")
        return None

def init_db():
    """
    Prompt for a filename, try to open it,
    and loop only on failure—exit on '0'.
    """
    while True:
        print("\nDATABASE CONNECTION\n===================")
        choice = input("Enter DB filename (ex. XYZGym.sqlite) (or '0' to quit): ").strip()
        if choice == '0':
            sys.exit(0)

        
        matches = [f for f in os.listdir('.') if f.lower() == choice.lower()]
        if not matches:
            print(f"'{choice}' not found. Please enter a valid file name.")
            continue

        conn = open_db(matches[0])
        if conn:
            return conn