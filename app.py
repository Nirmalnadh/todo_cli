# app.py

import sys
from storage import load_tasks, save_tasks
from utils import create_task, display_tasks

def main():
    tasks = load_tasks()

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python app.py add 'task name'")
        print("  python app.py list")
        print("  python app.py done <task_id>")
        print("  python app.py delete <task_id>")
        return

    command = sys.argv[1]

    if command == "add":
        title = " ".join(sys.argv[2:])
        task = create_task(title)
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!")

    elif command == "list":
        display_tasks(tasks)

    elif command == "done":
        task_id = sys.argv[2]
        for task in tasks:
            if task.id.startswith(task_id):
                task.completed = True
                print("✅ Task marked as done.")
                break
        else:
            print("❌ Task not found.")
        save_tasks(tasks)

    elif command == "delete":
        task_id = sys.argv[2]
        tasks = [task for task in tasks if not task.id.startswith(task_id)]
        print("🗑️ Task deleted.")
        save_tasks(tasks)

    else:
        print("❌ Unknown command.")

if __name__ == "__main__":
    main()
