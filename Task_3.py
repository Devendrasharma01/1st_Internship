class Task:

  def __init__(self, description):
    self.description = description
    self.completed = False

  def mark_completed(self):
    self.completed = True

  def __str__(self):
    status = "Completed" if self.completed else "Pending"
    return f"- {self.description} ({status})"


def create_task():
 
    description = input("Enter task description: ")
    return Task(description)


def display_tasks(tasks):
  
  if not tasks:
    print("There are no tasks to display.")
    return
  print("Your tasks:")
  for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")


def update_task(tasks):

  display_tasks(tasks)
  if not tasks:
    return

  try:
    task_index = int(input("Enter the number of the task to update: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
      raise IndexError("Invalid task number.")

    choice = input("Update description (d) or mark complete (c)? ").lower()
    if choice == "d":
      new_description = input("Enter new description: ")
      tasks[task_index].description = new_description
    elif choice == "c":
      tasks[task_index].mark_completed()
    else:
      print("Invalid choice.")
  except ValueError:
    print("Invalid input. Please enter a number.")
  except IndexError:
    print("Task not found.")


def delete_task(tasks):

  display_tasks(tasks)
  if not tasks:
    return

  try:
    task_index = int(input("Enter the number of the task to delete: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
      raise IndexError("Invalid task number.")
    del tasks[task_index]
    print("Task deleted successfully.")
  except ValueError:
    print("Invalid input. Please enter a number.")
  except IndexError:
    print("Task not found.")


def main():

  tasks = []
  while True:
    print("\nTask Manager")
    print("1. Create Task")
    print("2. Display Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
      tasks.append(create_task())
    elif choice == "2":
      display_tasks(tasks)
    elif choice == "3":
      update_task(tasks)
    elif choice == "4":
      delete_task(tasks)
    elif choice == "5":
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")



main()
