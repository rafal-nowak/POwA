import random


def random_generator(ammount):
    if ammount < 0:
        print("")
        return 1
    elif ammount > 100:
        return 1
    else:
        numbers = []
        i = 0
        while i < ammount:
            n = random.randrange(1, 50)
            if n % 2 == 0:
                numbers.append(n)
                i = i + 1

        return numbers


def menu():
    print("")
    print("menu")
    print("0 - zakończ program")
    print("1 - wygeneruj liczby pseudolosowe(maksymalnie 100)")
    print("2 - zapisz ostatnie do pliku")
    print("")


def file_saver(numbers):
    with open("losowenumerki.txt", "w") as file:
        for number in numbers:
            file.write(str(number))
            file.write("\n")


if __name__ == '__main__':
    print("losowanie liczb pseudolosowych")
    end = 0
    while end == 0:
        print(menu())
        choose = int(input("Wybierz opcje: "))
        match choose:
            case 0:
                print("no ok")
                end = 1
            case 1:
                print("ile chcesz liczb")
                ammount = int(input())
                temp = 0
                while temp == 0:
                    if random_generator(ammount) == 1:
                        print("zła ilość")
                        ammount = int(input())
                    else:
                        temp = 1
                numbers = random_generator(ammount)
                print(numbers)
            case 2:
                file_saver(numbers)
            case _:
                print("wybierz dobrą opcje")
