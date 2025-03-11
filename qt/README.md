# Tworzenie aplikacji w Qt (Python, PyQt6)

## Bardziej rozbudowany przykład: Aplikacja do monitorowania wartości czujnika

**Opis:**
Aplikacja wykorzystuje logikę biznesową do obsługi czujnika temperatury. Dane są pobierane z klasy SensorLogic i wyświetlane w interfejsie Qt. Aktualizacja wartości odbywa się poprzez kliknięcie przycisku.

```python
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys
import random

# Logika biznesowa: Klasa czujnika
class SensorLogic:
    def __init__(self):
        self.value = 25  # Początkowa temperatura

    def read_value(self):
        # Symulacja odczytu wartości czujnika
        self.value = random.uniform(20.0, 30.0)
        return round(self.value, 2)

# Interfejs użytkownika w PyQt6
class SensorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.sensor = SensorLogic()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Monitorowanie czujnika")
        layout = QVBoxLayout()
        
        self.label = QLabel("Aktualna wartość: -- °C", self)
        layout.addWidget(self.label)
        
        self.button = QPushButton("Odczytaj wartość", self)
        self.button.clicked.connect(self.update_value)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        self.resize(300, 200)
    
    def update_value(self):
        value = self.sensor.read_value()
        self.label.setText(f"Aktualna wartość: {value} °C")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SensorApp()
    window.show()
    sys.exit(app.exec())
```


## Opis działania:

- **Klasa `SensorLogic`** symuluje czujnik temperatury, który zwraca losowe wartości w zakresie 20-30°C.

- **Klasa `SensorApp`** zarządza interfejsem użytkownika i komunikuje się z logiką biznesową.

- Po naciśnięciu przycisku, aplikacja odczytuje nową wartość temperatury i aktualizuje etykietę w GUI.

Ten przykład pokazuje separację warstw aplikacji: interfejs użytkownika nie wykonuje logiki obliczeniowej, a jedynie prezentuje dane.

