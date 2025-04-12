# from task_manager.logic import TaskManager
from logic import TaskManager

def show_menu():
    print("\n--- Menedżer Zadań ---")
    print("1. Pokaż listę zadań")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Zmień status zadania (✔/✗)")
    print("5. Wyjście")

def main():
    task_manager = TaskManager()

    while True:
        show_menu()
        choice = input("Wybierz opcję (1-5): ").strip()

        match choice:
            case "1":
                tasks = task_manager.get_tasks()
                if not tasks:
                    print("Brak zadań.")
                else:
                    print("\nTwoje zadania:")
                    for idx, task in enumerate(tasks):
                        print(f"{idx}. {task}")
            case "2":
                task_name = input("Wpisz treść zadania: ").strip()
                if task_name:
                    task_manager.add_task(task_name)
                    print("Dodano zadanie.")
                else:
                    print("Nie można dodać pustego zadania.")
            case "3":
                index = input("Podaj numer zadania do usunięcia: ").strip()
                if index.isdigit():
                    task_manager.remove_task(int(index))
                    print("Zadanie usunięte (jeśli istniało).")
                else:
                    print("Błędny numer.")
            case "4":
                index = input("Podaj numer zadania do zmiany statusu: ").strip()
                if index.isdigit():
                    task_manager.toggle_task(int(index))
                    print("Zmieniono status zadania (jeśli istniało).")
                else:
                    print("Błędny numer.")
            case "5":
                print("Do zobaczenia!")
                break
            case _:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()
