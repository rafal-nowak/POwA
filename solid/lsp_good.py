# Liskov Substitution Principle (LSP) – obiekty klasy bazowej można zastąpić obiektami pochodnymi

class Bird:
    def move(self):
        return "Moving"

class FlyingBird(Bird):
    def move(self):
        return "Flying"

class WalkingBird(Bird):
    def move(self):
        return "Walking"