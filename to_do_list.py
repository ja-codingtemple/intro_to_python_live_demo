'''
Feel free to use this as starter-code for your To-Do-List Project.
'''

# Create a tasks list.
tasks = []

# Function to display options.
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    
# Function to add a task to the tasks list.
def add_task():
     task = input("Enter a task: ")
     tasks.append(task)
     print(f"Task {task} added successfully.")
     
# Function to view all tasks in the tasks list.
def view_tasks():
    # (IMPLEMENT THIS FUNCTION)
    print("This function should display all tasks in the tasks list.")
    
# Function to delete a task.
def delete_task():
    # (IMPLEMENT THIS FUNCTION)
    print("This function should delete a task.")


# Main function (start of the program)
def main():
    # Infinite loop.
    while True:
        display_menu()
        choice = input("What would you like to do?: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
main()