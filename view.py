"""View: input/output formatting only; does not mutate tasks."""
from collections.abc import Callable
from mvc.model import Task


class ConsoleView:
    def __init__(
        self,
        input_fn: Callable[[str], str] = input,
        output_fn: Callable[[str], None] = print,
    ) -> None:
        self._input = input_fn
        self._output = output_fn

    def menu(self) -> str:
        self._output("\n--- Менеджер завдань (MVC) ---")
        self._output("1 — Показати завдання")
        self._output("2 — Додати завдання")
        self._output("3 — Позначити виконаним")
        self._output("4 — Видалити завдання")
        self._output("0 — Вийти")
        return self._input("Ваш вибір: ").strip()

    def ask(self, prompt: str) -> str:
        return self._input(prompt)

    def show_tasks(self, tasks: list[Task]) -> None:
        if not tasks:
            self._output("Список завдань порожній.")
            return
        for task in tasks:
            status = "✓" if task.completed else " "
            self._output(f"[{status}] {task.id}. {task.title}")

    def message(self, text: str) -> None:
        self._output(text)
