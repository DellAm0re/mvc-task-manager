"""Model: application data and business rules; no UI dependencies."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    id: int
    title: str
    completed: bool = False


class TaskRepository:
    """In-memory task storage with validation and stable IDs."""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, title: str) -> Task:
        clean_title = title.strip()
        if not clean_title:
            raise ValueError("Назва завдання не може бути порожньою.")
        task = Task(id=self._next_id, title=clean_title)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def all(self) -> list[Task]:
        return list(self._tasks.values())

    def complete(self, task_id: int) -> Task:
        if task_id not in self._tasks:
            raise KeyError(f"Завдання №{task_id} не знайдено.")
        previous = self._tasks[task_id]
        task = Task(id=previous.id, title=previous.title, completed=True)
        self._tasks[task_id] = task
        return task

    def delete(self, task_id: int) -> None:
        if task_id not in self._tasks:
            raise KeyError(f"Завдання №{task_id} не знайдено.")
        del self._tasks[task_id]
