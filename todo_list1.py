# 📌 Advanced To-Do List Application

# Task list
todo_list = []

def add_task():
    """ Get a task from the user and add it to the list """
    task = input("📝 Enter a new task: ")
    todo_list.append({"task": task, "done": False})
    print("✅ Task added!")

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
            print("🎉 Task marked as completed!")
        else:
            print("⚠ Invalid number!")
    except ValueError:
        print("⚠ Please enter a valid number!")

def delete_task():
    """ Remove a task from the list """
    view_tasks()
    try:
        task_num = int(input("\nEnter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            removed_task = todo_list.pop(task_num)
            print(f"🗑 Task deleted: {removed_task['task']}")
        else:
            print("⚠ Invalid number!")
    except ValueError:
        print("⚠ Please enter a valid number!")

# Main program loop
while True:
    print("\n📌 To-Do List Application")
    print("1️⃣ Add a new task")
    print("2️⃣ View tasks")
    print("3️⃣ Mark a task as completed")
    print("4️⃣ Delete a task")
    print("5️⃣ Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

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
        print("⚠ Invalid input! Please choose 1, 2, 3, 4, or 5.")

