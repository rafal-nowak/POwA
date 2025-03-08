# Interface Segregation Principle (ISP) – podział interfejsów na mniejsze

class Scanner:
    def scan(self):
        pass

class Printer:
    def print(self):
        pass

class MultiFunctionDevice(Scanner, Printer):
    def scan(self):
        return "Scanning..."
    def print(self):
        return "Printing..."