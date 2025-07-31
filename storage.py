# storage.py

import csv
import os
from task import Task

FILE_PATH = "tasks.csv"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task.from_dict(row))
    return tasks

def save_tasks(tasks):
    with open(FILE_PATH, "w", newline="") as file:
        fieldnames = ["id", "title", "completed", "created_at"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow(task.to_dict())
