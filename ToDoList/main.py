# To-Do List Application

# Initialize an empty list to store tasks

tasks = []


# Function to add tasks to the list
def add_task(task_description):
    """
        Add a new task to the list with a unique identifier.

        Parameters:
        - task_description: The description of the task to be added.
        """

    task_id = len(tasks) + 1
    new_task = {'id': task_id, 'description': task_description, 'completed': False}
    # Add the new task to the list
    tasks.append(new_task)
    print("Task added successfully.")


# Function to mark tasks as completed
def completed_task(task_id):
    """
    Mark a task as completed based on its unique identifier.

    Parameters:
    - task_id: The unique identifier of the task to be marked as completed.
    """
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            print("Task marked as completed.")
            return
    print("Task not found.")


# Function to delete tasks from the list
def delete_task(task_id):
    """
    Delete a task from the list based on its unique identifier.

    Parameters:
    - task_id: The unique identifier of the task to be deleted.
    """
    task_found = False
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            task_found = True
            print("Task deleted successfully.")
            break
    if not task_found:
        print("Task not found.")


# Function to display the list of tasks
def display_tasks():
    """Display all tasks in the list."""
    if not tasks:
        print("No task found.")
    else:
        print("Tasks: ")
        for task in tasks:
            status = 'Completed' if task['completed'] else "Not completed"
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {status}")


# Main function to run the application
def main():
    """Main function to run the To-Do List application."""
    print("Welcome to the To Do List Application!")

    while True:
        print("Menu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")
        #print("Menu:\n1. Add Task\n2. Mark Task as Completed\n3. Delete Task\n4. View Tasks\n5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task_description = input("Enter task description: ")
            add_task(task_description)
        elif choice == '2':
            task_id = input("Enter task ID to mark as completed: ")
            if task_id.isdigit():
                completed_task(int(task_id))
            else:
                print("Invalid task ID. Please enter a valid number.")
        elif choice == '3':
            task_id = input("Enter task ID to delete: ")
            if task_id.isdigit():
                delete_task(int(task_id))
            else:
                    print("Invalid task ID. Please enter a valid number.")
        elif choice == '4':
            display_tasks()
        elif choice == '5':
            print("Thank you for using the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
