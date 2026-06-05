# Enkapsulacja: pola `_` i `__` w dziedziczeniu

Najczęstsza pułapka studentów przy enkapsulacji: zachowanie pól prywatnych (`__`) przy
dziedziczeniu. Ten materiał wyjaśnia, *dlaczego* i *jak* używać `_protected` i
`__private` poprawnie.

> Adaptacja materiału z `oop-python`. Teoria enkapsulacji jako filaru → [`README.md`](README.md),
> bazowy przykład `BankAccount` → [`main_oop4.py`](main_oop4.py).

## Trzy poziomy widoczności

```python
class Sensor:
    def __init__(self):
        self.name = "TC-01"     # 🟢 publiczne   — wolno używać wszędzie
        self._status = "idle"   # 🟡 chronione   — konwencja: „nie ruszaj z zewnątrz”
        self.__offset = 0.5     # 🔴 prywatne    — name mangling
```

W Pythonie to **konwencje wspierane przez język**, nie twarde blokady jak w C++/Java.
`_status` to czysta umowa społeczna. `__offset` Python faktycznie utrudnia — przez
*name mangling* zmienia nazwę na `_Sensor__offset`.

## Kluczowa pułapka: `__` przy dziedziczeniu

To **nie jest nadpisanie pola**:

```python
class Parent:
    def __init__(self):
        self.__value = 10

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = 999      # NIE nadpisuje pola rodzica!
```

Python tworzy **dwa różne pola**:

```
_Parent__value = 10
_Child__value  = 999
```

Student myśli „nadpisuję wartość z `Parent`”, a w rzeczywistości **tworzy nowe, osobne pole**.
To zwykle źródło trudnych do wytropienia błędów.

## Jak robić to dobrze

### ✅ Sposób #1 — używaj metod (najlepszy)

```python
class Parent:
    def __init__(self):
        self.__value = 10

    def get_value(self):
        return self.__value

    def set_value(self, val):
        if val >= 0:                 # reguła pilnowana w jednym miejscu
            self.__value = val

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.set_value(999)          # przez metodę — enkapsulacja zachowana

    def double_value(self):
        return self.get_value() * 2
```

Zalety: zachowujesz enkapsulację, nie psujesz logiki, kod jest bezpieczny.

### ✅ Sposób #2 — `_` zamiast `__`, gdy dziecko MA mieć dostęp

```python
class Parent:
    def __init__(self):
        self._value = 10

class Child(Parent):
    def __init__(self):
        super().__init__()
        self._value = 999            # to działa zgodnie z intuicją
```

Używaj, gdy kontrolujesz cały kod i świadomie chcesz, by podklasa sięgała do pola.

### ⚠️ Sposób #3 — name mangling ręcznie (unikać)

```python
self._Parent__value = 999           # działa, ale łamie enkapsulację
```

Technicznie możliwe, ale utrudnia utrzymanie kodu i sygnalizuje, że projekt klasy jest zły.

## Przykład z życia — `BankAccount`

Bazowy `BankAccount` (z [`main_oop4.py`](main_oop4.py)) chroni saldo przez `__balance`:

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
```

### ❌ Źle — podklasa obchodzi enkapsulację name manglingiem

```python
class PremiumAccount(BankAccount):
    def add_bonus(self):
        self._BankAccount__balance += 1000   # ominięcie reguły deposit()
```

### ✅ Dobrze — podklasa korzysta z publicznego API rodzica

```python
class PremiumAccount(BankAccount):
    def add_bonus(self):
        self.deposit(1000)                   # przechodzi przez walidację
```

## Myślenie „seniorskie” — `@property`

Zamiast pary `get_value`/`set_value` często stosuje się właściwość:

```python
class Sensor:
    def __init__(self, offset):
        self.__offset = offset

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, value):
        if value >= 0:
            self.__offset = value
```

Dzięki temu piszemy `sensor.offset` i `sensor.offset = 0.7` jak na zwykłym polu, a mimo
to zachowujemy kontrolę dostępu (walidacja w setterze).

## TL;DR

- `__value` w `Parent` ≠ `__value` w `Child` — to dwa różne pola (name mangling).
- Przy `__private` **używaj metod**, nie pól bezpośrednio.
- `_value` (chronione) — OK do dziedziczenia, gdy świadomie tego chcesz.
- `__value` (prywatne) — chroni przed przypadkowym dostępem, także z podklasy.
- `@property` = wygoda pola + kontrola metody.

## Zadanie refleksyjne

1. Dlaczego `_` nie daje realnej ochrony, a `__` „prawie” ją daje?
2. Kiedy świadomie wybrać `__`, a kiedy `_`?
3. Czy polimorfizm zależy od prywatności pól? (To dwie różne osie — patrz [`README.md`](README.md).)
