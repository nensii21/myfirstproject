# Simple To-Do List App
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Added task: {task}")

def main():
    while True:
        print("\nOptions: [1] Show Tasks [2] Add Task [3] Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
