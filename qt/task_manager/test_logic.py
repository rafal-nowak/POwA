import pytest
import sys
import os

# Dodaj katalog "qt" do sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task_manager.logic import TaskManager

@pytest.fixture
def task_manager():
    """Tworzy nową instancję TaskManager dla każdego testu."""
    return TaskManager()

def test_example():
    assert 2 + 2 == 4

def test_add_task(task_manager):
    task_manager.add_task("Kup mleko")
    tasks = task_manager.get_tasks()
    assert tasks == ["[✗] Kup mleko"]

def test_remove_task(task_manager):
    task_manager.add_task("Kup mleko")
    task_manager.add_task("Zrób pranie")
    task_manager.remove_task(0)
    tasks = task_manager.get_tasks()
    assert tasks == ["[✗] Zrób pranie"]

def test_remove_task_invalid_index(task_manager):
    task_manager.add_task("Kup mleko")
    task_manager.remove_task(10)  # poza zakresem
    tasks = task_manager.get_tasks()
    assert tasks == ["[✗] Kup mleko"]

def test_toggle_task(task_manager):
    task_manager.add_task("Kup mleko")
    task_manager.toggle_task(0)
    assert task_manager.get_tasks() == ["[✔] Kup mleko"]
    task_manager.toggle_task(0)
    assert task_manager.get_tasks() == ["[✗] Kup mleko"]

def test_toggle_task_invalid_index(task_manager):
    task_manager.toggle_task(10)  # Indeks poza zakresem
    tasks = task_manager.get_tasks()
    assert tasks == []

def test_get_tasks(task_manager):
    task_manager.add_task("Kup mleko")
    task_manager.add_task("Zrób pranie")
    task_manager.toggle_task(1)
    tasks = task_manager.get_tasks()
    assert tasks == ["[✗] Kup mleko", "[✔] Zrób pranie"]
