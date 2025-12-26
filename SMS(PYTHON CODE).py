import json
import os

# --- Configuration ---
FILE_NAME = "students.json"
# The data is stored as a dictionary where keys are student IDs for easy lookups
students_data = {}

# --- Helper Functions ---

def load_data():
    """Loads student data from the JSON file if it exists."""
    global students_data
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                students_data = json.load(file)
            print(f"Data loaded successfully from {FILE_NAME}.")
        except json.JSONDecodeError:
            print("Error reading JSON file. Starting with empty records.")
            students_data = {}
    else:
        print(f"No previous data file found ({FILE_NAME}). Starting fresh.")

def save_data():
    """Saves current student data to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(students_data, file, indent=4)
    print("Data saved successfully.")

def clear_screen():
    """Clears the console screen for better readability."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Core Features (CRUD Operations) ---

def add_student():
    """Prompts the user for student details and adds a new record."""
    clear_screen()
    print("--- Add New Student ---")
    student_id = input("Enter Student ID (e.g., 001): ").strip()
    
    if student_id in students_data:
        print(f"[Error] A student with ID {student_id} already exists.")
        return

    name = input("Enter Name: ").strip()
    grade = input("Enter Grade/Level: ").strip()
    
    if not student_id or not name or not grade:
        print("[Error] ID, Name, and Grade cannot be empty.")
        return

    students_data[student_id] = {
        "Name": name,
        "Grade": grade
    }
    save_data()
    print(f"[Success] Student ID {student_id} added.")

def view_students():
    """Displays all existing student records."""
    clear_screen()
    print("--- All Student Records ---")
    if not students_data:
        print("No student records found.")
        return

    # Display data in a simple table format
    print(f"{'ID':<10} | {'Name':<20} | {'Grade':<10}")
    print("-" * 45)
    for student_id, details in students_data.items():
        print(f"{student_id:<10} | {details['Name']:<20} | {details['Grade']:<10}")

def search_student():
    """Searches for a student by their ID."""
    clear_screen()
    print("--- Search Student ---")
    student_id = input("Enter Student ID to search: ").strip()

    if student_id in students_data:
        details = students_data[student_id]
        print("\nStudent Found:")
        print(f"ID:    {student_id}")
        print(f"Name:  {details['Name']}")
        print(f"Grade: {details['Grade']}")
    else:
        print(f"[Info] Student with ID {student_id} not found.")

def delete_student():
    """Deletes a student record based on their ID."""
    clear_screen()
    print("--- Delete Student ---")
    student_id = input("Enter Student ID to delete: ").strip()

    if student_id in students_data:
        confirm = input(f"Are you sure you want to delete student {student_id}? (y/n): ").strip().lower()
        if confirm == 'y':
            del students_data[student_id]
            save_data()
            print(f"[Success] Student ID {student_id} deleted.")
        else:
            print("[Info] Deletion cancelled.")
    else:
        print(f"[Error] Student with ID {student_id} not found.")

# --- Main Application Loop ---

def main():
    load_data()
    while True:
        print("\n*** Student Management System Menu ***")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search for a Student")
        print("4. Delete a Student")
        print("5. Exit Program")
        print("--------------------------------------")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("[Error] Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

