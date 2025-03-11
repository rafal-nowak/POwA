class Observer:
    def update(self, value):
        pass

class Sensor:
    def __init__(self):
        self.observers = []
        self.value = None

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.value)

    def set_value(self, value):
        self.value = value
        self.notify_observers()

class Display(Observer):
    def update(self, value):
        print(f"New sensor value: {value}")

if __name__ == "__main__":
    # Przykład użycia
    sensor = Sensor()
    display = Display()
    sensor.add_observer(display)
    sensor.set_value(42)