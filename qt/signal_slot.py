from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys


class SignalSlotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Sygnały i sloty w PyQt6")
        layout = QVBoxLayout()

        self.label = QLabel("Naciśnij przycisk", self)
        layout.addWidget(self.label)

        self.button = QPushButton("Kliknij mnie", self)
        self.button.clicked.connect(self.change_text)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.resize(300, 200)

    def change_text(self):
        self.label.setText("Przycisk został kliknięty!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignalSlotApp()
    window.show()
    sys.exit(app.exec())