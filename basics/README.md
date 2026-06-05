# Pakiet `basics` — podstawy Pythona

Materiały wprowadzające do Pythona. Pliki są celowo napisane tak, że **większość kodu
jest zakomentowana** — jest to świadomy zabieg dydaktyczny, a nie pomyłka.

## Jak korzystać z tych plików (metoda „odkomentuj → wytłumacz → zakomentuj")

Każdy plik to sekwencja niezależnych fragmentów oddzielonych pustymi liniami.
Na zajęciach:

1. **Odkomentuj** jeden fragment (np. blok `if/elif/else`).
2. **Uruchom** go zieloną strzałką w PyCharm i **omów** wynik ze studentami.
3. **Zakomentuj** z powrotem, żeby konsola była czysta.
4. Przejdź do **następnego** fragmentu.

Dzięki temu każdy temat omawiamy w izolacji, bez szumu z pozostałych przykładów.
Aktywny (odkomentowany) fragment to zwykle ten, który właśnie ćwiczymy — reszta czeka
zakomentowana.

## Kolejność proponowana na zajęciach

| # | Plik | Temat | Co odkomentowujemy po kolei |
|---|------|-------|------------------------------|
| 1 | [`main.py`](main.py) | Fundament języka | zmienne i typy → `input()` → `if/elif/else` → listy → zbiory → krotki → słowniki → pętle `for`/`while` → funkcje → wbudowane (`len`, `max`, `min`) |
| 2 | [`main__1.py`](main__1.py) | Wariant `main.py` | ta sama mapa, ale z odkomentowanym `input()` na starcie — wygodny punkt wejścia do interakcji z użytkownikiem |
| 3 | [`main_adv.py`](main_adv.py) | Funkcje zaawansowane | argument domyślny (`greeting="Hello"`) → `*args` (dowolna liczba argumentów) → wyrażenie `lambda` |
| 4 | [`main_dict.py`](main_dict.py) | Słowniki w praktyce | słownik prosty → słownik zagnieżdżony → sprawdzanie klucza (`in`) → `.get()` → `.get(key, default)` → obsługa `KeyError` przez `try/except` |
| 5 | [`main_exceptions.py`](main_exceptions.py) | Wyjątki | nieobsłużony błąd (`10/0`) → `try/except ZeroDivisionError` → `ValueError` przy `int("abc")` → wiele klauzul `except` → `try/except/finally` przy pliku |
| 6 | [`main_files.py`](main_files.py) | Pliki i CSV | odczyt pliku tekstowego (`read`) → zapis (`write`) → zapis `data.csv` przez `csv.writer` → odczyt przez `csv.reader` |
| 7 | [`main_files_basic.py`](main_files_basic.py) | Pliki — warianty odczytu | `read()` (całość) → list comprehension `[line.rstrip() ...]` → `readlines()`; osobno `write_to_file()` zapisujący kolejne liczby |

## Czego dotykają poszczególne tematy

**`main.py` / `main__1.py`** — kompletny przegląd od podstaw:
- zmienne i typy podstawowe: `str`, `int`, `bool`, `float`,
- wejście od użytkownika (`input`) i konkatenacja stringów,
- instrukcja warunkowa `if/elif/else`,
- kolekcje: `list` (indeksowanie, *slicing*, `append`), `set` (unikalność), `tuple`,
- słowniki (`dict`) i dostęp przez klucz,
- pętle `for` (po `range` i po kolekcji) oraz `while`,
- definiowanie funkcji (`greet`, `add`) i funkcje wbudowane (`len`, `max`, `min`).

> Różnica `main.py` vs `main__1.py`: w `main__1.py` aktywny jest fragment z `input()`,
> a deklaracje zmiennych są zakomentowane — dobry plik na pokazanie interakcji.

**`main_adv.py`** — co odróżnia funkcję „ładną" od „surowej":
- argumenty domyślne (`greeting="Hello"`),
- zmienna liczba argumentów (`*args`) i ich sumowanie w pętli,
- funkcja anonimowa `lambda x: x ** 2`.

**`main_dict.py`** — bezpieczna praca ze słownikami:
- przekazywanie słownika do funkcji, słowniki zagnieżdżone (`subjects`),
- trzy sposoby na „czy klucz istnieje": operator `in`, `.get()` (zwraca `None`),
  `.get(key, default)` oraz `try/except KeyError`.

To dobre wprowadzenie do dwóch przeciwstawnych stylów programowania w Pythonie. Oba
rozwiązują ten sam problem („czy klucz jest w słowniku?"), ale podchodzą do niego odwrotnie:

- **LBYL** — *Look Before You Leap* („sprawdź, zanim skoczysz"). Najpierw **weryfikujesz
  warunek**, a dopiero potem działasz:

  ```python
  if "age" in student_info:        # najpierw sprawdzenie
      print(student_info["age"])   # potem użycie
  ```

- **EAFP** — *Easier to Ask Forgiveness than Permission* („łatwiej prosić o wybaczenie
  niż o pozwolenie"). **Działasz od razu**, a ewentualny błąd przechwytujesz wyjątkiem:

  ```python
  try:
      print(student_info["age"])   # próbujesz od razu
  except KeyError:                 # reagujesz dopiero, gdy się nie uda
      print("Brak klucza 'age'")
  ```

  EAFP to styl **uznawany w Pythonie za bardziej idiomatyczny** — unika podwójnego
  sprawdzania (raz w `if`, raz przy dostępie) i jest odporny na sytuację, w której klucz
  zniknie między sprawdzeniem a użyciem.

**`main_exceptions.py`** — obsługa błędów krok po kroku:
- co się dzieje **bez** `try` (nieobsłużony wyjątek przerywa wykonanie programu),
- łapanie konkretnego wyjątku (`ZeroDivisionError`, `ValueError`),
- wiele klauzul `except` + `except Exception as e`,
- `finally` — sprzątanie (zamknięcie pliku) niezależnie od błędu.

**`main_files.py` / `main_files_basic.py`** — wejście/wyjście:
- odczyt i zapis plików tekstowych przez `with open(...)`,
- różne strategie czytania: `read()`, `readlines()`, list comprehension po liniach,
- praca z CSV (`csv.writer` / `csv.reader`) na przykładzie pomiarów temperatury.

> Uwaga: `main_files*.py` zakładają istnienie pliku `example.txt` w katalogu `basics/`.
> Najpierw odkomentuj fragment zapisu (`write`), żeby plik powstał, potem odczyt.

## Dalej

Po opanowaniu podstaw → pakiet [`../oop/`](../oop/README.md) (programowanie obiektowe i
cztery filary OOP).
