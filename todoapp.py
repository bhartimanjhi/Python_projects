# PYTHON TO-DO-LIST COMMAND LINE INTERFACE APPLICATION:-

print("------MY TO-DO-LIST APPLICATION------")
print("Welcome to the python TO-DO-LIST Application!\nNow you can add and manage your tasks here...!!!")
tasks = []


def add_task():
    tasks.append({"task": task, "completed": False})
    print("Task Is Added")


def list_tasks():
    print("\nLIST OF YOUR TASKS:-")
    for index, task1 in enumerate(tasks, start=1):
        if task1["completed"]:
            status = "✓"
        else:
            status = " "
        print(f"{index}.[{status}] {task1['task']}")
        print()


def mark_completed(index1):
    if 1 <= index1 <= len(tasks):
        tasks[index1 - 1]["completed"] = True
        print("Task is successfully marked as completed,\nto check please go to your list of tasks...")
    else:
        print("invalid task")


while True:
    print("\nOPTIONS:-")
    print("1. Add your task")
    print("2. List of tasks")
    print('3. Mark your task as "task is completed!"')
    print("4. Exit")

    choice = input("Please select any one option(1/2/3/4): ")
    if choice == "1":
        task = input("Please enter your task: ")
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        list_tasks()
        index2 = int(input("Enter the task number which you have completed: "))
        mark_completed(index2)
    elif choice == "4":
        print("bye-bye!, Thank you for using python TO-DO-LIST Application!")
        break
    else:
        print("invalid choice")

input()
