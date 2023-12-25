class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

def display_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    manager = TaskManager()

    while True:
        user_choice = display_menu()

        if user_choice == '1':
            task = input("Enter the task: ")
            manager.add_task(task)

        elif user_choice == '2':
            manager.view_tasks()

        elif user_choice == '3':
            try:
                task_number = int(input("Enter the task number to delete: "))
                manager.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")

        elif user_choice == '4':
            print("Exiting the Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
