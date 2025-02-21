import json  

TODO_FILE = "todo_list.json"

todo_list = []

def load_tasks():
    """ Load tasks from the file """
    global todo_list
    try:
        with open(TODO_FILE, "r") as file:
            todo_list = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        todo_list = []  

def save_tasks():
    """ Save tasks to the file """
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file, indent=4)

def add_task():
    """ Get a task from the user and add it to the list """
    try:
        task = input("📝 Enter a new task: ").strip()
        if not task:
            raise ValueError("⚠ Task cannot be empty!")
        todo_list.append({"task": task, "done": False})
        save_tasks()
        print("✅ Task added!")
    except ValueError as e:
        print(e)

def mark_task_done():
    """ Mark a task as completed """
    try:
        view_tasks()
        task_num = int(input("\nEnter the number of the completed task: ")) - 1
        if task_num < 0 or task_num >= len(todo_list):
            raise IndexError("⚠ Invalid task number!")
        todo_list[task_num]["done"] = True
        save_tasks()
        print("🎉 Task marked as completed!")
    except ValueError:
        print("⚠ Error: Please enter a valid number!")
    except IndexError as e:
        print(e)

# Main program
load_tasks()

while True:
    print("\n📌 To-Do List Application")
    print("1️⃣ Add a new task")
    print("2️⃣ View tasks")
    print("3️⃣ Mark a task as completed")
    print("4️⃣ Exit")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        print("👋 Exiting the application...")
        break
    else:
        print("⚠ Invalid input! Please choose 1, 2, 3, or 4.")

