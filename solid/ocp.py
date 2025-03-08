# Open/Closed Principle (OCP) – klasa powinna być otwarta na rozszerzenie, ale zamknięta na modyfikację

from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, price):
        pass

class StudentDiscount(Discount):
    def calculate(self, price):
        return price * 0.9