from PyQt6.QtWidgets import QApplication
from ui import TicTacToeUI
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToeUI()
    window.show()
    sys.exit(app.exec())
