from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Prosta aplikacja PyQt6")
        self.label = QLabel("Witaj w PyQt6!", self)
        self.label.move(50, 50)
        self.resize(300, 200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.show()
    sys.exit(app.exec())