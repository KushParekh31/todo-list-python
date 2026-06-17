import json
import os
from datetime import datetime

FILE_NAME = "task.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return[]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter task: ")

    tasks.append({
        "task": task,
        "completed": False,
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "completed_at": None
    })

    save_tasks(tasks)
    print("Task added successfully!")
    
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for i, task in enumerate(tasks, start=1):

        status = "✓" if task["completed"] else "✗"

        print(f"\n{i}. [{status}] {task['task']}")
        print(f"   Created: {task['created_at']}")

        if task["completed"]:
            print(f"   Completed: {task['completed_at']}")
    
def complete_task(tasks):
    view_tasks(tasks)

    try:
        index = int(input("Enter task number to complete: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            tasks[index]["completed_at"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            save_tasks(tasks)
            print("Task marked as completed!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted: {removed['task']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
