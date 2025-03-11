class TaskManager:
    def __init__(self):
        self.tasks = []  # Lista zadań

    def add_task(self, task_name):
        """Dodaje nowe zadanie do listy."""
        self.tasks.append({"task": task_name, "done": False})

    def remove_task(self, index):
        """Usuwa zadanie z listy na podstawie indeksu."""
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def toggle_task(self, index):
        """Oznacza zadanie jako wykonane/niewykonane."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = not self.tasks[index]["done"]

    def get_tasks(self):
        """Zwraca listę zadań w formacie tekstowym do wyświetlenia w GUI."""
        return [f"[{'✔' if task['done'] else '✗'}] {task['task']}" for task in self.tasks]
