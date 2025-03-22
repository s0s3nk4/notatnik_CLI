import os
import datetime
from sqlite3.dbapi2 import Timestamp
import time

NOTES_FILE = "notes.txt"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        for note in notes:
            file.writelines(note + "\n")

def add_note():
    note = input("Enter your note: ").strip() 
    if not note:
        print("Note can't be empty")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes = load_notes()
    notes.append(f"{timestamp} {note}")
    save_notes(notes)
    print("Note added!")

def edit_note():
    notes = load_notes()
    if not notes:
        print("No notes to edit")
        return
    list_notes()
    try:
        index = int(input("Enter the number of the note to edit: ")) - 1
        if index < 0 or index >= len(notes):
            print("Invalid note number")
            return
        note = input("Enter the new note: ").strip() 
        if not note:
            print("Note can't be empty")
            return
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes[index] = f"{timestamp} {note}"
        save_notes(notes)
        print("Note edited!")
    except ValueError:
        print("Invalid input")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes")
    else:
        for i, note in enumerate(notes):
           print(f"{i + 1}. {note}")

def search_notes():
    notes = load_notes()
    if not notes:
        print("No notes to search")
        return
    search = input("Enter the search string: ").lower()
    found = False
    for note in notes:
        if search in note.lower():
            print(note, end="")
            found = True
    if not found:
        print("No notes found")

def delete_note():
    notes = load_notes()
    if not notes:
        print("No notes to delete")
        return
    list_notes()
    try:
        index = int(input("Enter the number of the note to delete: ")) - 1
        if index < 0 or index >= len(notes):
            print("Invalid note number")
            return
        notes.pop(index)
        save_notes(notes)
        print("Note deleted!")
    except ValueError:
        print("Invalid input")

def main():
    while True:
        print("\n Notepad")
        print("1. Add note")
        print("2. List notes")
        print("3. Edit note")
        print("4. Search notes")
        print("5. Delete note")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4": 
            search_notes()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()