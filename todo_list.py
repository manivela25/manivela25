import json  # To store data in JSON format

# 📌 Advanced To-Do List Application with File Handling
TODO_FILE = "todo_list.json"

# List to store tasks
todo_list = []

def load_tasks():
    """ Load tasks from the file """
    global todo_list
    try:
        with open(TODO_FILE, "r") as file:
            todo_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        todo_list = []  # If the file doesn't exist or is empty, start a new list

def save_tasks():
    """ Save tasks to the file """
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file, indent=4)

def add_task():
    """ Get a task from the user and add it to the list """
    task = input("📝 Enter a new task: ").strip()
    if task:
        todo_list.append({"task": task, "done": False})
        save_tasks()  # Save to file
        print("✅ Task added!")
    else:
        print("⚠ Error: Task cannot be empty!")

def view_tasks():
    """ Display the task list """
    if not todo_list:
        print("📭 The list is empty.")
        return
    print("\n📌 To-Do List:")
    for index, task in enumerate(todo_list, 1):
        status = "✅ Completed" if task["done"] else "❌ Pending"
        print(f"{index}. {task['task']} - {status}")

def mark_task_done():
    """ Mark a task as completed """
    view_tasks()
    try:
        task_num = int(input("\nEnter the number of the completed task: ")) - 1
        if 0 <= task_num < len(todo_list):
            todo_list[task_num]["done"] = True
            save_tasks()  # Save to file
            print("🎉 Task marked as completed!")
        else:
            print("⚠ Error: Invalid task number!")
    except ValueError:
        print("⚠ Error: Please enter a valid number!")

def delete_task():
    """ Remove a task from the list """
    view_tasks()
    try:
        task_num = int(input("\nEnter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed_task = todo_list.pop(task_num)
            save_tasks()  # Save to file
            print(f"🗑 Task deleted: {removed_task['task']}")
        else:
            print("⚠ Error: Invalid task number!")
    except ValueError:
        print("⚠ Error: Please enter a valid number!")

# Main program loop
load_tasks()  # Load tasks when the program starts

while True:
    print("\n📌 To-Do List Application")
    print("1️⃣ Add a new task")
    print("2️⃣ View tasks")
    print("3️⃣ Mark a task as completed")
    print("4️⃣ Delete a task")
    print("5️⃣ Exit")

    choice = input("Enter your choice (1/2/3/4/5): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Exiting the application...")
        break
    else:
        print("⚠ Error: Invalid input! Please choose 1, 2, 3, 4, or 5.")

