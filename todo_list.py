# To-Do List application
todo_list = []

while True:
    print("\n📌 To-Do List Application")
    print("1️⃣ Add a new task")
    print("2️⃣ View tasks")
    print("3️⃣ Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        task = input("Enter the task you want to add: ")
        todo_list.append(task)
        print("✅ Task added!")

    elif choice == "2":
        print("\n📌 Your To-Do List:")
        if len(todo_list) == 0:
            print("📭 The list is empty.")
        else:
            for index, task in enumerate(todo_list, 1):
                print(f"{index}. {task}")

    elif choice == "3":
        print("👋 Exiting the application...")
        break

    else:
        print("⚠ Invalid input! Please choose 1, 2, or 3.")

