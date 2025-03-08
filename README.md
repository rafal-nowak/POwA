# Programowanie obiektowe w automatyce

## 1. Wprowadzenie do programowania obiektowego (OOP)

Definicja: Paradygmat programowania oparty na obiektach i ich interakcjach.

Zalety:

- Lepsza organizacja kodu

- Wielokrotne użycie kodu (reusability)

- Łatwiejsza konserwacja

Kluczowe pojęcia:

- **Klasa i obiekt** – klasa jako szablon, obiekt jako instancja

- **Hermetyzacja** – ukrywanie szczegółów implementacji

- **Dziedziczenie** – tworzenie nowych klas na bazie istniejących

- **Polimorfizm** – różne implementacje tej samej metody

Przykład w Pythonie:

```python
class Sensor:
    def __init__(self, name):
        self.name = name
    
    def read_value(self):
        return 42
```


Przykład w C++:
```
class Sensor {
public:
    std::string name;
    int readValue() { return 42; }
};
```


## 2. Dobre praktyki w programowaniu obiektowym

**Zasady SOLID:**

**S – Single Responsibility Principle** (Pojedyncza odpowiedzialność)

**O – Open/Closed Principle** (Otwarte/Zamknięte)

**L – Liskov Substitution Principle** (Zasada podstawienia Liskov)

**I – Interface Segregation Principle** (Segregacja interfejsów)

**D – Dependency Inversion Principle** (Odwrócenie zależności)

Przykłady implementacji SOLID w Pythonie:

Single Responsibility Principle (SRP) – każda klasa ma jedną odpowiedzialność:

```python
class ReportGenerator:
    def generate(self, data):
        return f"Report: {data}"

class ReportPrinter:
    def print(self, report):
        print(report)
```


Open/Closed Principle (OCP) – klasa powinna być otwarta na rozszerzenie, ale zamknięta na modyfikację:

```python
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

class StudentDiscount(Discount):
    def calculate(self, price):
        return price * 0.9
```

Liskov Substitution Principle (LSP) – obiekty klasy bazowej można zastąpić obiektami pochodnymi:

Błędne podejście:

```python
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly")
```

Właściwe podejście:

```python
class Bird:
    def move(self):
        return "Moving"

class FlyingBird(Bird):
    def move(self):
        return "Flying"

class WalkingBird(Bird):
    def move(self):
        return "Walking"
```

Interface Segregation Principle (ISP) – podział interfejsów na mniejsze:

```python
class Scanner:
    def scan(self):
        pass

class Printer:
    def print(self):
        pass

class MultiFunctionDevice(Scanner, Printer):
    def scan(self):
        return "Scanning..."
    def print(self):
        return "Printing..."
```

Dependency Inversion Principle (DIP) – wysokopoziomowe moduły nie zależą od niskopoziomowych:

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        return "Connecting to MySQL"

class Application:
    def __init__(self, database: Database):
        self.database = database
    
    def start(self):
        print(self.database.connect())

# Przykład użycia
mysql_db = MySQLDatabase()
app = Application(mysql_db)
app.start()
```


Wzorce projektowe w automatyce:

**Singleton** – np. zarządzanie połączeniem z urządzeniem

**Fabryka** – dynamiczne tworzenie obiektów

**Obserwator** – np. monitorowanie wartości czujnika

## 3. Wprowadzenie do Qt w kontekście automatyki

Qt: Framework dla C++ (GUI, komunikacja, sterowanie urządzeniami)

Signal-Slot Mechanism – podstawowa metoda komunikacji wewnątrz aplikacji

Qt Designer – narzędzie do tworzenia GUI

## 4. Tworzenie aplikacji w Qt (C++)

Struktura aplikacji Qt:

QMainWindow – główne okno aplikacji

QWidget – komponenty interfejsu

QSerialPort – obsługa portów szeregowych

Przykład aplikacji:

```
#include <QApplication>
#include <QPushButton>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QPushButton button("Kliknij mnie");
    button.show();
    return app.exec();
}
```

## 5. Wykorzystanie Python + Qt (PyQt/PySide)

Zalety: Prostota Pythona + wydajność Qt

Przykładowe zastosowania: Modbus, MQTT, OPC UA

Przykład w PyQt:

```python
from PyQt5.QtWidgets import QApplication, QPushButton
import sys

app = QApplication(sys.argv)
button = QPushButton("Kliknij mnie")
button.show()
sys.exit(app.exec_())
```


6. Podsumowanie i sesja Q&A

C++ czy Python? Kiedy który język wybrać?

Jak rozwijać swoje umiejętności?

Praktyczne zadania dla uczestników.