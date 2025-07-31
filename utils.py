# utils.py

import uuid
from task import Task

def create_task(title):
    return Task(id=str(uuid.uuid4()), title=title)

def display_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for task in tasks:
            status = "✅" if task.completed else "❌"
            print(f"[{status}] {task.title} (ID: {task.id[:8]}) - {task.created_at}")
