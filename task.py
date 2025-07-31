# task.py

from datetime import datetime

class Task:
    def __init__(self, id, title, completed=False, created_at=None):
        self.id = id
        self.title = title
        self.completed = completed
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": str(self.completed),
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            title=data["title"],
            completed=data["completed"] == "True",
            created_at=data["created_at"]
        )
