class TicTacToe:
    """Silnik gry w kółko i krzyżyk - logika oddzielona od UI."""

    EMPTY = " "
    PLAYER_X = "X"
    PLAYER_O = "O"

    WINNING_LINES = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # wiersze
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # kolumny
        (0, 4, 8), (2, 4, 6),             # przekątne
    )

    def __init__(self):
        self.board = [self.EMPTY] * 9
        self.current_player = self.PLAYER_X
        self.winner = None
        self.winning_line = None

    def make_move(self, index):
        """Wykonuje ruch bieżącego gracza na pole `index`. Zwraca True jeśli ruch był poprawny."""
        if self.is_game_over():
            return False
        if not (0 <= index < 9):
            return False
        if self.board[index] != self.EMPTY:
            return False

        self.board[index] = self.current_player
        self._update_winner()
        if not self.is_game_over():
            self._switch_player()
        return True

    def reset(self):
        """Resetuje stan gry do warunków początkowych."""
        self.board = [self.EMPTY] * 9
        self.current_player = self.PLAYER_X
        self.winner = None
        self.winning_line = None

    def is_draw(self):
        return self.winner is None and all(cell != self.EMPTY for cell in self.board)

    def is_game_over(self):
        return self.winner is not None or self.is_draw()

    def get_board(self):
        """Zwraca kopię planszy jako listę 9 pól."""
        return list(self.board)

    def status(self):
        """Tekstowy opis bieżącego stanu - przydatny w dowolnym UI."""
        if self.winner is not None:
            return f"Wygrał gracz {self.winner}!"
        if self.is_draw():
            return "Remis!"
        return f"Ruch gracza: {self.current_player}"

    def _update_winner(self):
        for line in self.WINNING_LINES:
            a, b, c = line
            if self.board[a] != self.EMPTY and self.board[a] == self.board[b] == self.board[c]:
                self.winner = self.board[a]
                self.winning_line = line
                return

    def _switch_player(self):
        self.current_player = self.PLAYER_O if self.current_player == self.PLAYER_X else self.PLAYER_X
