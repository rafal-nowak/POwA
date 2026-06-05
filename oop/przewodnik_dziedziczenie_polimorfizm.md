# Dziedziczenie i polimorfizm — przewodnik krok po kroku

Materiał prowadzi od najprostszej klasy do klas abstrakcyjnych, w kolejności, która
sprawdza się dydaktycznie. Każdy krok ma odpowiednik w plikach `oop/*.py` — można
odkomentowywać fragmenty po kolei i omawiać.

> Adaptacja materiału z projektu `oop-python`, dopasowana do przykładów w tym repo.
> Część teoretyczna (cztery filary, model parowania) → [`README.md`](README.md).

## Cel materiału

Po przerobieniu student powinien:
- rozumieć, czym jest **dziedziczenie** i **polimorfizm**,
- umieć tworzyć klasy bazowe i potomne oraz nadpisywać metody,
- rozróżniać zwykłą klasę bazową od **klasy abstrakcyjnej**,
- wiedzieć, **kiedy** dziedziczenia używać, a kiedy nie.

Ścieżka tłumaczenia (sprawdzona kolejność): zwykła klasa → klasa bazowa i potomna →
nadpisanie metody → polimorfizm w pętli → klasy abstrakcyjne jako „kontrakt”.

---

## 1. Zwykła klasa — punkt wyjścia

Klasa modeluje obiekt: ma **atrybuty** (dane) i **metody** (zachowania).
Por. [`main_oop1.py`](main_oop1.py) (`Person`) i [`main_oop2.py`](main_oop2.py) (`Circle`).

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says: Hau!"

dog = Dog("Burek")
print(dog.speak())
```

## 2. Dziedziczenie — „X jest rodzajem Y”

Nowa klasa przejmuje cechy istniejącej, może dodawać własne i zmieniać odziedziczone.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}"

class Dog(Animal):
    pass            # nie ma własnego kodu, a i tak ma introduce()

print(Dog("Burek").introduce())   # I am Burek
```

`Dog` dziedziczy wszystko z `Animal`. Można dołożyć własną metodę:

```python
class Dog(Animal):
    def bark(self):
        return "Woof!"
```

## 3. Nadpisywanie metod (overriding)

Klasa potomna może zmienić zachowanie metody odziedziczonej. To realne w
[`main_oop3.py`](main_oop3.py):

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

Wszystkie mają `speak()`, ale każda realizuje go inaczej — to prowadzi nas do polimorfizmu.

## 4. Polimorfizm — wspólny interfejs

Różne obiekty można obsłużyć **tym samym kodem**, jeśli mają wspólną metodę:

```python
for animal in [Dog("Burek"), Cat("Mruczek")]:
    print(animal.speak())
```

Pętla nie wie, czy trzyma psa czy kota — wystarczy, że obiekt ma `speak()`.

> W Pythonie to działa **nawet bez wspólnej klasy bazowej** (duck typing) —
> patrz [`main_oop3a.py`](main_oop3a.py) i sekcja „Niuans Pythona” w [`README.md`](README.md).

To samo na figurach — [`main_oop5.py`](main_oop5.py):

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

def print_area(shape):       # zadziała dla KAŻDEJ figury z metodą area()
    print("Area:", shape.area())

for s in [Rectangle(4, 5), Circle(3)]:
    print_area(s)
```

## 5. Po co klasa bazowa?

Klasa bazowa zbiera wspólne cechy, upraszcza kod i pozwala pisać funkcje działające na
wielu typach (jak `print_area` wyżej). Ale...

## 6. Problem: klasa zbyt ogólna

```python
class Shape:
    def area(self):
        pass

shape = Shape()      # technicznie działa, ale „jakaś figura” nie ma sensu
```

Chcemy tworzyć prostokąty i koła, a nie „figurę w ogóle”. Rozwiązanie: **klasa abstrakcyjna**.

## 7. Klasa abstrakcyjna jako kontrakt

Klasa, której **nie tworzymy bezpośrednio** i która **wymusza** implementację metod
w podklasach. W Pythonie służy do tego moduł `abc` — por. [`main_oop6.py`](main_oop6.py)
i [`main_oop8.py`](main_oop8.py):

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height
    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)
print(rect.area())       # 20

class Triangle(Shape):
    pass

# Triangle()   <-- TypeError: nie zaimplementowano area()
```

Zaleta kontraktu: jeśli podklasa zapomni o `area()`, błąd pojawia się **od razu**, a nie
dopiero przy wywołaniu. Interfejs rodziny klas jest spójny.

## 8. `super()` — rozszerzanie, nie przepisywanie

Gdy podklasa chce *dorzucić* coś do logiki rodzica zamiast pisać od zera:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # użyj konstruktora rodzica
        self.breed = breed

dog = Dog("Burek", "Beagle")
print(dog.name, dog.breed)
```

Bez `super()` duplikowalibyśmy przypisanie `self.name = name`.

## 9. Kiedy dziedziczenie, a kiedy NIE

- ✅ Relacja **„X jest rodzajem Y”**: pies–zwierzę, prostokąt–figura, menedżer–pracownik.
- ❌ Relacja **„X ma Y”**: samochód *ma* silnik, komputer *ma* procesor. Tu lepsza jest
  **kompozycja** (składanie obiektów), nie dziedziczenie.

Nie dziedzicz „bo się da” — dziedziczenie ma oddawać logiczną relację, nie oszczędzać pisania.

## 10. Pełny przykład — polimorfizm + abstrakcja + `super()`

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours, self.rate = hours, rate
    def calculate_salary(self):
        return self.hours * self.rate

for e in [FullTimeEmployee("Anna", 7000), HourlyEmployee("Piotr", 80, 50)]:
    print(e.name, e.calculate_salary())
```

Widać tu naraz: **dziedziczenie** (obie po `Employee`), **klasę abstrakcyjną** (nie
tworzymy `Employee`), **polimorfizm** (każdy liczy pensję inaczej) i **`super()`**.

---

## Najczęstsze błędy studentów

1. **Mylenie dziedziczenia z kopiowaniem kodu** — ma oddawać relację, nie skracać pisanie.
2. **Brak nadpisania metody** — jeśli podklasa ma działać inaczej, trzeba nadpisać.
3. **Tworzenie obiektu klasy zbyt ogólnej** — rozważ klasę abstrakcyjną.
4. **Nieużywanie `super()`** — prowadzi do duplikacji kodu rodzica.
5. **Brak wspólnego interfejsu** — polimorfizm działa najlepiej, gdy klasy mają wspólny
   zestaw metod.

## Szybka ściąga

```python
class Child(Parent): ...                 # dziedziczenie

class Child(Parent):                     # nadpisanie
    def method(self): return "new"

from abc import ABC, abstractmethod      # klasa abstrakcyjna
class Base(ABC):
    @abstractmethod
    def method(self): ...

super().__init__(...)                    # wywołanie konstruktora rodzica
```

## Pytania kontrolne

1. Czym różni się klasa bazowa od klasy abstrakcyjnej?
2. Dlaczego polimorfizm jest przydatny?
3. Co daje nadpisywanie metod?
4. Po co używa się `super()`?
5. Kiedy dziedziczenie ma sens, a kiedy lepiej go unikać?

## Zadania → [`cwiczenia_oop.md`](cwiczenia_oop.md)
