# To-Do List App using Python

def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("\nNo tasks found!")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("\nNo tasks file found!")


def add_task():
    task = input("Enter new task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")


def delete_task():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        show_tasks()
        task_no = int(input("Enter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)

            with open("tasks.txt", "w") as file:
                file.writelines(tasks)

            print("Task deleted!")
        else:
            print("Invalid task number!")

    except:
        print("Error occurred!")


while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")