class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self):
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        self.tasks.append(Task(name, description))
        print("Task created successfully!")

    def read_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"Task {i+1}:")
            print(f"Name: {task.name}")
            print(f"Description: {task.description}")

    def update_task(self):
        task_id = int(input("Enter task ID to update: ")) - 1
        if task_id < 0 or task_id >= len(self.tasks):
            print("Invalid task ID!")
            return
        name = input("Enter new task name: ")
        description = input("Enter new task description: ")
        self.tasks[task_id] = Task(name, description)
        print("Task updated successfully!")

    def delete_task(self):
        task_id = int(input("Enter task ID to delete: ")) - 1
        if task_id < 0 or task_id >= len(self.tasks):
            print("Invalid task ID!")
            return
        del self.tasks[task_id]
        print("Task deleted successfully!")

def main():
    task_manager = TaskManager()
    while True:
        print("\n1. Create task")
        print("2. Read tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        option = int(input("Choose an option: "))
        if option == 1:
            task_manager.create_task()
        elif option == 2:
            task_manager.read_tasks()
        elif option == 3:
            task_manager.update_task()
        elif option == 4:
            task_manager.delete_task()
        elif option == 5:
            break
        else:
            print("Invalid option!")


main()
