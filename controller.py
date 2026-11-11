"""Controller: translates user actions into model operations and view output."""
from mvc.model import TaskRepository
from mvc.view import ConsoleView


class TaskController:
    def __init__(self, model: TaskRepository, view: ConsoleView) -> None:
        self.model = model
        self.view = view

    def handle(self, choice: str) -> bool:
        """Handle one menu selection. False means exit the application."""
        if choice == "0":
            self.view.message("До побачення!")
            return False
        if choice == "1":
            self.view.show_tasks(self.model.all())
            return True
        if choice == "2":
            title = self.view.ask("Назва завдання: ")
            try:
                task = self.model.add(title)
                self.view.message(f"Додано завдання №{task.id}.")
            except ValueError as error:
                self.view.message(f"Помилка: {error}")
            return True
        if choice in ("3", "4"):
            raw_id = self.view.ask("Номер завдання: ")
            try:
                task_id = int(raw_id)
                if choice == "3":
                    task = self.model.complete(task_id)
                    self.view.message(f"Завдання №{task.id} виконано.")
                else:
                    self.model.delete(task_id)
                    self.view.message(f"Завдання №{task_id} видалено.")
            except ValueError:
                self.view.message("Помилка: номер має бути цілим числом.")
            except KeyError as error:
                self.view.message(f"Помилка: {error.args[0]}")
            return True
        self.view.message("Невідомий пункт меню.")
        return True

    def run(self) -> None:
        while self.handle(self.view.menu()):
            pass
