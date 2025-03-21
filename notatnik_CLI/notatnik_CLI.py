import os

NOTES_FILE = "notes.txt"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as file:
        return file.readlines()

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        for note in notes:
            file.writelines(note)

def add_note():
    note = input("Enter your note: ") + "\n"
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Note added!")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes")
    else:
        for i, note in enumerate(notes):
           print(f"{i + 1}. {note}", end="")

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
        print("3. Delete note")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()