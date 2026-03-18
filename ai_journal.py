# Day 4 - AI Journal (Save and Read Data)

def save_entry(entry):
    with open("journal.txt", "a") as file:
        file.write(entry + "\n")

def read_entries():
    try:
        with open("journal.txt", "r") as file:
            entries = file.readlines()
            
            print("\n=== Your AI Journal ===")
            for e in entries:
                print("-", e.strip())
    except FileNotFoundError:
        print("\nNo journal entries yet.")

def main():
    print("=== AI Journal Day 4 ===")
    
    while True:
        print("\nOptions:")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            entry = input("Write your learning today: ")
            save_entry(entry)
            print("Entry saved!")
        
        elif choice == "2":
            read_entries()
        
        elif choice == "3":
            print("Goodbye! Keep building 🚀")
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()