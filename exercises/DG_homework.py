import random


def menu():
    print()
    print("Wybierz opcje:")
    print("0. Zakoncz program")
    print("1. Wygeneruj wartosci pseudolosowe")
    print("2. Zapisz wygenerowane wartosci do pliku")
    print()


def spawner():
    rand = 2 * random.randrange(1, 25)
    return rand


def writer(number):
    with open("export.txt", "a") as file:
        file.write(number + "\n")


if __name__ == "__main__":
    numbers = []
    n = 0
    print("LOSOWANIE LICZB LOSOWYCH")
    print()
    end = False
    while not end:
        menu()
        opt = int(input())
        match opt:
            case 0:
                print()
                print("Zamykam program...")
                end = True
            case 1:
                print()
                n = int(input("Podaj ilosc liczb, ktore maja zostac wygenerowane: "))
                if n < 0 or n > 100:
                    print("Podano nieodpowiednia wartosc")
                if n == 1:
                    print("Generuje 1 liczbe...")
                if 1 < n < 5:
                    print("Generuje " + str(n) + " liczby...")
                if 4 < n < 101:
                    print("Generuje " + str(n) + " liczb...")
                i = 0
                while i < n:
                    numbers.append(spawner())
                    print(numbers[i])
                    i = i + 1
            case 2:
                print()
                if not numbers:
                    print("Jeszcze nie wygenerowano zadnych liczb!")
                elif numbers:
                    i = 0
                    while i < n:
                        number = str(numbers[i])
                        writer(number)
                        i = i + 1
                    print("Wylosowane liczby wyeksportowano do export.txt")
            case _:
                print()
                print("Podano bledna opcje!")