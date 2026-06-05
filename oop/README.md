# Cztery filary programowania obiektowego

Materiał teoretyczny do pakietu `oop/`. Każdy filar jest tu powiązany z **konkretnym
plikiem** w tym katalogu — można od razu odkomentować przykład, uruchomić i omówić.

> **Kluczowa idea dydaktyczna tego materiału:** czterech filarów nie uczymy jako
> luźnej wyliczanki. Tworzą **dwie pary**, które tłumaczy się razem, bo jeden filar
> w parze jest *intencją*, a drugi *mechanizmem*, który tę intencję realizuje.

```
        OŚ „UKRYWANIA”                    OŚ „WSPÓLNEGO INTERFEJSU”

   Abstrakcja  ←→  Enkapsulacja      Dziedziczenie  ←→  Polimorfizm
   (co pokazać)    (jak chronić)     (skąd wziąć)       (jak użyć tak samo)
```

| Filar | Pytanie, na które odpowiada | Plik w repo |
|-------|------------------------------|-------------|
| Abstrakcja | „Co obiekt **robi**, a co mnie nie obchodzi?” | [`main_oop6.py`](main_oop6.py), [`main_oop8.py`](main_oop8.py) |
| Enkapsulacja | „Kto i jak może **dotykać** danych?” | [`main_oop4.py`](main_oop4.py) |
| Dziedziczenie | „Czy X **jest rodzajem** Y?” | [`main_oop3.py`](main_oop3.py), [`main_oop5.py`](main_oop5.py), [`main_oop9.py`](main_oop9.py) |
| Polimorfizm | „Czy mogę traktować różne obiekty **tak samo**?” | [`main_oop3.py`](main_oop3.py), [`main_oop3a.py`](main_oop3a.py), [`main_oop5.py`](main_oop5.py) |

---

## Para 1 — oś „ukrywania”: Abstrakcja ↔ Enkapsulacja

Te dwa filary opisują **to samo zjawisko z dwóch stron**: chowanie szczegółów.
Różnią się poziomem.

- **Abstrakcja** to decyzja *projektowa*: ustalam, **co** świat zewnętrzny ma widzieć
  (kontrakt, interfejs, „istota rzeczy”). Czujnik *udostępnia* metodę `read()` — i tyle
  ma obchodzić użytkownika. Czy w środku jest I²C, Modbus czy losowa liczba — to już
  nie jego sprawa.
- **Enkapsulacja** to *mechanizm* w kodzie, który tę decyzję **egzekwuje**: pola
  prywatne, właściwości, kontrola dostępu. To „zamek w drzwiach”, który pilnuje, żeby
  nikt nie wszedł tylnym wejściem.

> **Związek:** enkapsulacja jest technicznym **wymuszeniem** abstrakcji.
> Abstrakcja mówi *„tego nie pokazujemy”*, enkapsulacja sprawia, że *naprawdę się nie da*.
> Abstrakcja bez enkapsulacji to obietnica bez ochrony.

### Abstrakcja w praktyce — klasa abstrakcyjna jako kontrakt

Plik [`main_oop6.py`](main_oop6.py) / [`main_oop8.py`](main_oop8.py):

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):        # KONTRAKT: każda figura policzy pole...
        pass

    @abstractmethod
    def perimeter(self):   # ...i obwód — ale JAK, to już szczegół podklasy
        pass
```

`Shape` mówi *co* (każda figura ma pole i obwód), nie mówi *jak*. Nie da się utworzyć
„jakiejś figury” — `Shape()` rzuca błąd. To jest abstrakcja: pracujemy z pojęciem, nie
z implementacją.

### Enkapsulacja w praktyce — pola prywatne i metody dostępowe

Plik [`main_oop4.py`](main_oop4.py):

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # chronione (konwencja)
        self.__balance = balance               # prywatne (name mangling)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:            # <-- TU mieszka reguła biznesowa
            self.__balance += amount
```

Saldo można zmienić **tylko** przez `deposit()`, a `deposit()` pilnuje reguły
(`amount > 0`). Gdyby `__balance` było publiczne, każdy mógłby wpisać `account.balance = -999`
i obejść logikę. Enkapsulacja chroni *niezmienniki* obiektu.

Poziomy widoczności w Pythonie (uwaga: to **konwencja**, nie twarda blokada jak w C++/Java):

| Zapis | Znaczenie | Egzekwowanie |
|-------|-----------|--------------|
| `self.name` | publiczne | brak |
| `self._status` | chronione — „nie ruszaj z zewnątrz” | tylko umowa społeczna |
| `self.__balance` | prywatne — *name mangling* na `_BankAccount__balance` | utrudnione, nie niemożliwe |

Szczegóły i pułapki pól `_`/`__` w dziedziczeniu → [`enkapsulacja_i_pola_w_dziedziczeniu.md`](enkapsulacja_i_pola_w_dziedziczeniu.md).

---

## Para 2 — oś „wspólnego interfejsu”: Dziedziczenie ↔ Polimorfizm

Tu również: jeden filar dostarcza *struktury*, drugi *korzyści*.

- **Dziedziczenie** buduje hierarchię „**jest rodzajem**” i pozwala ponownie użyć kodu
  klasy bazowej. `Dog(Animal)` — pies *jest* zwierzęciem.
- **Polimorfizm** to **wypłata** z tej struktury: skoro `Dog` i `Cat` mają wspólną metodę
  `speak()`, mogę przejść po liście zwierząt jedną pętlą, nie pytając o typ.

### Dziedziczenie + polimorfizm „klasycznie”

Plik [`main_oop3.py`](main_oop3.py):

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):       # Dog JEST rodzajem Animal  → dziedziczenie
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

for animal in [Dog(), Cat()]:   # ten sam kod, różne zachowanie → polimorfizm
    print(animal.speak())
```

Pętla nie wie i nie musi wiedzieć, czy trzyma psa czy kota. Wystarczy, że obiekt
„umie” `speak()`. To samo na figurach w [`main_oop5.py`](main_oop5.py).

### ⚠️ Niuans Pythona, który WZMACNIA tę parę

W klasycznym OOP (C++, Java) polimorfizm podtypowy **wymaga** wspólnej klasy bazowej.
W Pythonie — **nie**. Dzięki *duck typingowi* („jeśli kwacze jak kaczka...”) liczy się
to, czy obiekt ma metodę, a nie po kim dziedziczy.

Plik [`main_oop3a.py`](main_oop3a.py) — ten sam efekt, **bez** dziedziczenia:

```python
class Dog():             # NIE dziedziczy po Animal!
    def speak(self):
        return "Woof!"

class Cat():             # też nie
    def speak(self):
        return "Meow!"

for animal in [Dog(), Cat()]:
    print(animal.speak())   # polimorfizm DZIAŁA mimo braku wspólnej bazy
```

> **Wniosek dla studenta:** „dziedziczenie + polimorfizm” to *najczęstszy* sposób, ale
> nie jedyny. Dziedziczenie jest jedną z dróg do polimorfizmu — w Pythonie liczy się
> **wspólny interfejs**, nie wspólny przodek. Ta uwaga nie psuje pary, tylko pokazuje,
> że to polimorfizm jest celem, a dziedziczenie — wygodnym środkiem.

Kiedy `Shape(ABC)` z [`main_oop6.py`](main_oop6.py) spina obie pary naraz: abstrakcja
(kontrakt) + enkapsulacja (ABC wymusza implementację) + dziedziczenie (`Circle(Shape)`)
+ polimorfizm (`for s in shapes: s.area()`).

---

## Ściąga końcowa

```
ABSTRAKCJA      = co pokazać        (kontrakt / interfejs)      → ABC, @abstractmethod
ENKAPSULACJA    = jak chronić       (kontrola dostępu)          → _protected, __private, @property
DZIEDZICZENIE   = skąd wziąć        (relacja „jest rodzajem”)   → class Child(Parent)
POLIMORFIZM     = jak użyć tak samo (wspólny interfejs)         → nadpisanie metody / duck typing

Para 1:  Abstrakcja  potrzebuje  Enkapsulacji,  żeby ukrycie było realne.
Para 2:  Dziedziczenie  daje  Polimorfizm — ale w Pythonie polimorfizm bywa i bez niego.
```

## Pytania kontrolne

1. Dlaczego mówimy, że enkapsulacja „egzekwuje” abstrakcję? Podaj przykład abstrakcji
   bez enkapsulacji i pokaż, co może pójść źle.
2. Czym różni się `_status` od `__status` w Pythonie? Co dokładnie robi *name mangling*?
3. Dlaczego `main_oop3a.py` działa, mimo że `Dog` i `Cat` nie dziedziczą po `Animal`?
4. Czy polimorfizm zależy od prywatności pól? (Wskazówka: to dwie różne osie.)
5. Kiedy wybrać dziedziczenie, a kiedy duck typing / kompozycję?

## Dalej w tym pakiecie

- [`przewodnik_dziedziczenie_polimorfizm.md`](przewodnik_dziedziczenie_polimorfizm.md) — przewodnik krok po kroku (od zwykłej klasy do klas abstrakcyjnych)
- [`enkapsulacja_i_pola_w_dziedziczeniu.md`](enkapsulacja_i_pola_w_dziedziczeniu.md) — `_` vs `__`, name mangling, `@property`
- [`cwiczenia_oop.md`](cwiczenia_oop.md) — zadania od poziomu 1 do projektu mini
