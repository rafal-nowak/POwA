from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import sys

class ButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Przycisk w PyQt6")
        self.button = QPushButton("Kliknij mnie", self)
        self.button.clicked.connect(self.on_click)
        self.button.move(50, 50)
        self.resize(300, 200)

    def on_click(self):
        print("Przycisk został kliknięty!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonApp()
    window.show()
    sys.exit(app.exec())