import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n===== YOUR TASKS =====")
    for i, task in enumerate(tasks, start=1):
        status = "✓ Completed" if task["done"] else "✗ Pending"
        print(f"{i}. {task['title']}")
        print(f"   Priority : {task['priority']}")
        print(f"   Due Date : {task['due_date']}")
        print(f"   Status   : {status}")
        print()

# Add task
def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter priority (High/Medium/Low): ")
    due_date = input("Enter due date: ")

    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")

# Mark task as completed
def complete_task(tasks):
    view_tasks(tasks)

    try:
        task_num = int(input("Enter task number to mark completed: "))
        tasks[task_num - 1]["done"] = True

        save_tasks(tasks)

        print("Task marked as completed!")

    except:
        print("Invalid task number!")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_num = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_num - 1)

        save_tasks(tasks)

        print(f"Deleted task: {removed['title']}")

    except:
        print("Invalid task number!")

# Search task
def search_task(tasks):
    keyword = input("Enter keyword to search: ").lower()

    found = False

    print("\n===== SEARCH RESULTS =====")

    for i, task in enumerate(tasks, start=1):
        if keyword in task["title"].lower():
            status = "✓ Completed" if task["done"] else "✗ Pending"

            print(f"{i}. {task['title']}")
            print(f"   Priority : {task['priority']}")
            print(f"   Due Date : {task['due_date']}")
            print(f"   Status   : {status}")
            print()

            found = True

    if not found:
        print("No matching tasks found.")

# Main Program
tasks = load_tasks()

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        complete_task(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        search_task(tasks)

    elif choice == "6":
        print("Exiting To-Do App...")
        break

    else:
        print("Invalid choice! Please try again.")
