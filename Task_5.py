import os
import json

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            self.tasks = []
        else:
            with open(filename, 'r') as f:
                self.tasks = json.load(f)

    def create_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def read_tasks(self):
        return self.tasks

    def update_task(self, task_id, updated_task):
        self.tasks[task_id] = updated_task
        self.save_tasks()

    def delete_task(self, task_id):
        del self.tasks[task_id]
        self.save_tasks()

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f)

# Usage
task_manager = TaskManager('tasks.txt')
task_manager.create_task('Task 1')
print(task_manager.read_tasks())
task_manager.update_task(0, 'Updated Task 1')
print(task_manager.read_tasks())
task_manager.delete_task(0)
print(task_manager.read_tasks())
