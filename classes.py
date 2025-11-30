import json
from typing import List


class Task:
    """Класс для представления одной задачи."""

    def __init__(self, title: str, description: str, due_date: str) -> None:
        self.title: str = title
        self.description: str = description
        self.due_date: str = due_date

    def __repr__(self) -> str:
        return f"Task(title={self.title!r}, due_date={self.due_date!r})"


class TaskManager:
    """Класс для управления списком задач и работой с JSON-файлом."""

    def __init__(self, filename: str = "tasks.json") -> None:
        self.filename: str = filename
        self.tasks: List[Task] = []
        self.load_from_file()

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        self.save_to_file()

    def delete_task(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_to_file()

    def save_to_file(self) -> None:
        """Сохранить все задачи — используем json.dumps + f.write, чтобы избежать проблем с типами."""
        data = [
            {"title": t.title, "description": t.description, "due_date": t.due_date}
            for t in self.tasks
        ]
        json_text = json.dumps(data, ensure_ascii=False, indent=4)
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(json_text)

    def load_from_file(self) -> None:
        """Загрузить задачи из JSON-файла, если он существует."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [
                    Task(item["title"], item["description"], item["due_date"])
                    for item in data
                ]
        except FileNotFoundError:
            self.tasks = []


if __name__ == "__main__":
    # Быстрая проверка
    mgr = TaskManager()
    mgr.add_task(Task("Тестовая", "Описание", "2025-10-11"))
    print(mgr.tasks)
