from PyQt6.QtWidgets import QApplication
from ui import TaskManagerUI
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManagerUI()
    window.show()
    sys.exit(app.exec())
