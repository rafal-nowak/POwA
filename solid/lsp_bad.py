# Liskov Substitution Principle (LSP) – obiekty klasy bazowej można zastąpić obiektami pochodnymi

class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly")