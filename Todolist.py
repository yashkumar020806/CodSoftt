tasks = []
done = []

def show_menu():
    print("\nTO-DO LIST")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    done.append(False)
    print("Task added!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            if done[i]:
                status = "Done"
            else:
                status = "Not Done"
            print(str(i + 1) + ". " + tasks[i] + " [" + status + "]")

def mark_done():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        number = int(input("Enter task number to mark done: "))
        if number >= 1 and number <= len(tasks):
            done[number - 1] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("Exiting")
        break
    else:
        print("Invalid choice. Please try again.")
