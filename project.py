tasks = []

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. Complete task")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == '2':
            task_id = int(input("Enter the task ID to complete: "))
            complete_task(task_id)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_task(task):
    task_id = len(tasks) + 1
    tasks.append({'id': task_id, 'task': task, 'completed': False})
    print(f"Task added: {task}")

def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task {task_id} not found.")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "Done" if task['completed'] else "Pending"
        print(f"{task['id']}. {task['task']} - {status}")

if __name__ == "__main__":
    main()
