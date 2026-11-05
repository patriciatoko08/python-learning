import json

FILENAME = "tasks.json"


def load_tasks():
    try:
        with open(FILENAME) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


tasks = load_tasks()

while True:
    print("\n1. Show tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")
    print("5. Clear all tasks")
    choice = input("Choose: ")

    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        task = input("New task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Added.")
    elif choice == "3":
        show_tasks(tasks)
        try:
            number = int(input("Number to remove: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            else:
                print("That number is not in the list.")
        except ValueError:
            print("Please enter a number.")
    elif choice == "4":
        break
    elif choice == "5":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")
    else:
        print("Please choose 1, 2, 3 or 4.")