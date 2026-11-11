"""Application entry point: compose Model, View, and Controller."""
from mvc.model import TaskRepository
from mvc.view import ConsoleView
from mvc.controller import TaskController


def main() -> None:
    controller = TaskController(TaskRepository(), ConsoleView())
    controller.run()


if __name__ == "__main__":
    main()
