# Ćwiczenia: dziedziczenie, polimorfizm, abstrakcja, enkapsulacja

Zadania ułożone od najprostszych do miniprojektu. Wykonuj je po kolei — każdy poziom
zakłada poprzedni. Część zadań ma akcent „automatyki” (czujniki, urządzenia), spójny
z tematyką repo.

> Adaptacja zestawu z `oop-python`. Teoria → [`README.md`](README.md) i
> [`przewodnik_dziedziczenie_polimorfizm.md`](przewodnik_dziedziczenie_polimorfizm.md).

## Instrukcja

- Pisz kod w osobnych plikach (np. `cw_01.py`) lub w konsoli.
- Po każdym zadaniu uruchom kod i sprawdź wynik.
- Jeśli coś nie działa, najpierw przeczytaj **komunikat błędu** — często mówi wprost, czego brakuje.

---

## Poziom 1 — podstawy dziedziczenia

**Zadanie 1.** Utwórz klasę `Animal` z atrybutem `name` i metodą `introduce()`
zwracającą `"I am <name>"`. Utwórz `Dog(Animal)` bez własnego kodu i sprawdź, że
`Dog("Burek").introduce()` działa.

**Zadanie 2.** Dodaj do `Dog` własną metodę `bark()` zwracającą `"Woof!"`. Pokaż, że
pies ma *jednocześnie* `introduce()` (odziedziczone) i `bark()` (własne).

**Zadanie 3.** Nadpisz w `Dog` i `Cat` metodę `speak()` z klasy `Animal` (bazowo zwraca
`"Some sound"`), tak by zwracały odpowiednio `"Woof!"` i `"Meow!"`.

## Poziom 2 — polimorfizm

**Zadanie 4.** Zrób listę `[Dog(), Cat()]` i w pętli wywołaj `speak()` na każdym elemencie.
Zwróć uwagę: pętla nie pyta o typ obiektu.

**Zadanie 5.** Napisz funkcję `make_it_speak(animal)`, która wywołuje `animal.speak()`.
Sprawdź, że działa dla psa, kota i **dowolnego** obiektu z metodą `speak()` —
nawet jeśli nie dziedziczy po `Animal` (duck typing, por. [`main_oop3a.py`](main_oop3a.py)).

## Poziom 3 — figury geometryczne

**Zadanie 6.** Utwórz klasę bazową `Shape` z metodą `area()` zwracającą `0`.

**Zadanie 7.** Utwórz `Rectangle(Shape)` i `Circle(Shape)` nadpisujące `area()`
(pole prostokąta i koła). Por. [`main_oop5.py`](main_oop5.py).

**Zadanie 8.** Napisz funkcję `print_area(shape)` i przejdź pętlą po liście różnych figur.

## Poziom 4 — klasy abstrakcyjne

**Zadanie 9.** Przerób `Shape` na klasę abstrakcyjną (`ABC` + `@abstractmethod area`).
Sprawdź, że `Shape()` rzuca błąd. Por. [`main_oop6.py`](main_oop6.py).

**Zadanie 10.** Zaimplementuj `area()` w `Rectangle` i `Circle`. Upewnij się, że teraz
tworzenie tych obiektów działa.

**Zadanie 11 (błąd kontrolny).** Utwórz `Triangle(Shape)` **bez** metody `area()` i
spróbuj go utworzyć. Przeczytaj komunikat błędu — to zaleta kontraktu: brak wychodzi od razu.

## Poziom 5 — `super()` i enkapsulacja

**Zadanie 12.** `Animal.__init__` przyjmuje `name`. W `Dog.__init__` przyjmij `name` i
`breed`, użyj `super().__init__(name)` i dodaj `self.breed`.

**Zadanie 13.** Utwórz `BankAccount` z prywatnym `__balance`, metodami `deposit(amount)`
(tylko gdy `amount > 0`) i `get_balance()`. Por. [`main_oop4.py`](main_oop4.py).

**Zadanie 14.** Utwórz `PremiumAccount(BankAccount)` z metodą `add_bonus()`. Dodaj bonus
**poprawnie** (przez `deposit`), a nie przez `_BankAccount__balance`. Wyjaśnij różnicę —
patrz [`enkapsulacja_i_pola_w_dziedziczeniu.md`](enkapsulacja_i_pola_w_dziedziczeniu.md).

## Poziom 6 — system pracowników

**Zadanie 15.** Klasa abstrakcyjna `Employee(ABC)` z `name` i `@abstractmethod
calculate_salary()`.

**Zadanie 16.** `FullTimeEmployee` (pensja miesięczna) i `HourlyEmployee` (godziny × stawka),
obie z `super().__init__(name)`.

**Zadanie 17.** Lista pracowników → pętla wypisująca `name` i wyliczoną pensję (polimorfizm).

## Poziom 7 — miniprojekt: system płatności

**Zadanie 18.** Klasa abstrakcyjna `Payment` z metodą `pay(amount)`. Klasy:
`CardPayment`, `CashPayment`, `BLIKPayment` — każda wypisuje inny komunikat.

**Zadanie 19.** Lista różnych metod płatności i wywołanie `pay(100)` dla każdej.

## Poziom 8 — myślenie projektowe

**Zadanie 20.** Dla każdej pary rozstrzygnij: dziedziczenie („jest rodzajem”) czy
kompozycja („ma”)?
- samochód / silnik
- pies / zwierzę
- komputer / procesor
- menedżer / pracownik

**Zadanie 21.** Zaprojektuj (bez pisania całego kodu) hierarchię urządzeń pomiarowych:
`Device(ABC)` z `read()`, a potem `TemperatureSensor`, `PressureSensor`, `FlowSensor`.
Które elementy są wspólne (idą do bazy), a które różne (idą do podklas)?

## Bonus (dla ambitnych)

**Zadanie 22.** Przepisz `BankAccount` tak, by `balance` było dostępne przez `@property`
(getter) z setterem walidującym wartość ≥ 0.

**Zadanie 23.** Pokaż na własnym przykładzie pułapkę `__value` z [poradnika o polach](enkapsulacja_i_pola_w_dziedziczeniu.md):
ustaw `__value` w rodzicu i w dziecku, wypisz `vars(obj)` i wskaż dwa różne pola.
