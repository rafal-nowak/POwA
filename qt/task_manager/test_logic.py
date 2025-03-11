import pytest
import sys
import os

# Dodaj katalog "qt" do sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Teraz możesz poprawnie zaimportować moduł
from task_manager.logic import TaskManager

@pytest.fixture
def task_manager():
    """Tworzy nową instancję TaskManager dla każdego testu."""
    return TaskManager()

def test_example():
    assert 2 + 2 == 4

def test_add_task(task_manager):
    """Sprawdza, czy dodawanie zadań działa poprawnie."""
    task_manager.add_task("Kup mleko")
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0] == {"task": "Kup mleko", "done": False}

def test_remove_task(task_manager):
    """Sprawdza, czy usuwanie zadań działa poprawnie."""
    task_manager.add_task("Kup mleko")
    task_manager.add_task("Zrób pranie")
    task_manager.remove_task(0)
    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0]["task"] == "Zrób pranie"

def test_remove_task_invalid_index(task_manager):
    """Sprawdza, czy usunięcie zadania spoza zakresu nie powoduje błędu."""
    task_manager.add_task("Kup mleko")
    task_manager.remove_task(10)  # Indeks poza zakresem
    assert len(task_manager.tasks) == 1  # Lista powinna pozostać bez zmian

def test_toggle_task(task_manager):
    """Sprawdza, czy oznaczanie zadań jako ukończone/niewykonane działa poprawnie."""
    task_manager.add_task("Kup mleko")
    task_manager.toggle_task(0)
    assert task_manager.tasks[0]["done"] is True
    task_manager.toggle_task(0)
    assert task_manager.tasks[0]["done"] is False

def test_toggle_task_invalid_index(task_manager):
    """Sprawdza, czy zmiana statusu zadania spoza zakresu nie powoduje błędu."""
    task_manager.toggle_task(10)  # Indeks poza zakresem
    assert len(task_manager.tasks) == 0  # Lista powinna pozostać pusta

def test_get_tasks(task_manager):
    """Sprawdza, czy pobieranie listy zadań zwraca poprawny format tekstowy."""
    task_manager.add_task("Kup mleko")
    task_manager.add_task("Zrób pranie")
    task_manager.toggle_task(1)  # Oznacz drugie zadanie jako wykonane

    tasks = task_manager.get_tasks()
    assert tasks == ["[✗] Kup mleko", "[✔] Zrób pranie"]
