from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox
from logic import TaskManager

class TaskManagerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menedżer Zadań")
        self.setGeometry(100, 100, 400, 300)

        # Tworzenie instancji logiki biznesowej
        self.task_manager = TaskManager()

        # Layout główny
        self.layout = QVBoxLayout()

        # Lista zadań
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # Pole do wpisywania nowego zadania
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Wpisz nowe zadanie...")
        self.layout.addWidget(self.task_input)

        # Przyciski akcji
        self.add_button = QPushButton("Dodaj Zadanie")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Usuń Zadanie")
        self.remove_button.clicked.connect(self.remove_task)
        self.layout.addWidget(self.remove_button)

        self.toggle_button = QPushButton("Zmień Status")
        self.toggle_button.clicked.connect(self.toggle_task)
        self.layout.addWidget(self.toggle_button)

        # Ustawienie layoutu
        self.setLayout(self.layout)

        # Aktualizacja listy przy uruchomieniu
        self.update_task_list()

    def add_task(self):
        task_name = self.task_input.text().strip()
        if task_name:
            self.task_manager.add_task(task_name)
            self.task_input.clear()
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Błąd", "Nie można dodać pustego zadania!")

    def remove_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            self.task_manager.remove_task(selected)
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Błąd", "Nie wybrano zadania do usunięcia!")

    def toggle_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            self.task_manager.toggle_task(selected)
            self.update_task_list()
        else:
            QMessageBox.warning(self, "Błąd", "Nie wybrano zadania do zmiany statusu!")

    def update_task_list(self):
        """Aktualizuje widok listy zadań."""
        self.task_list.clear()
        self.task_list.addItems(self.task_manager.get_tasks())
