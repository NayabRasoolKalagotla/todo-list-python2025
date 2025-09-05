# todo.py
def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found.")

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def delete_task(task_no):
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Removed: {removed.strip()}")
        else:
            print("Invalid task number!")
    except FileNotFoundError:
        print("No tasks to delete.")

while True:
    print("\n--- To-Do List ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter new task: ")
        add_task(task)
    elif choice == "3":
        task_no = int(input("Enter task number to delete: "))
        delete_task(task_no)
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
