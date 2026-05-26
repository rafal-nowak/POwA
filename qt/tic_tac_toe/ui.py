from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QHBoxLayout
)

from logic import TicTacToe


class TicTacToeUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kółko i krzyżyk")
        self.setFixedSize(360, 420)

        self.game = TicTacToe()
        self.cell_buttons = []

        layout = QVBoxLayout()

        self.status_label = QLabel(self.game.status())
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        layout.addWidget(self.status_label)

        grid = QGridLayout()
        grid.setSpacing(4)
        button_font = QFont("Arial", 32, QFont.Weight.Bold)
        for index in range(9):
            button = QPushButton(TicTacToe.EMPTY)
            button.setFixedSize(100, 100)
            button.setFont(button_font)
            button.clicked.connect(lambda _checked, i=index: self.handle_cell_click(i))
            self.cell_buttons.append(button)
            grid.addWidget(button, index // 3, index % 3)
        layout.addLayout(grid)

        controls = QHBoxLayout()
        self.reset_button = QPushButton("Nowa gra")
        self.reset_button.clicked.connect(self.reset_game)
        controls.addWidget(self.reset_button)
        layout.addLayout(controls)

        self.setLayout(layout)
        self.refresh()

    def handle_cell_click(self, index):
        if self.game.make_move(index):
            self.refresh()

    def reset_game(self):
        self.game.reset()
        self.refresh()

    def refresh(self):
        board = self.game.get_board()
        winning_cells = set(self.game.winning_line or ())
        for index, button in enumerate(self.cell_buttons):
            button.setText(board[index])
            button.setEnabled(board[index] == TicTacToe.EMPTY and not self.game.is_game_over())
            if index in winning_cells:
                button.setStyleSheet("background-color: #b6f5b6;")
            else:
                button.setStyleSheet("")
        self.status_label.setText(self.game.status())
