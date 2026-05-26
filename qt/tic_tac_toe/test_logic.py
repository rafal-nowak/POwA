import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tic_tac_toe.logic import TicTacToe


@pytest.fixture
def game():
    return TicTacToe()


def play(game, moves):
    """Pomocnik: wykonuje sekwencję ruchów (indeksy pól) naprzemiennie."""
    for index in moves:
        assert game.make_move(index), f"Ruch {index} powinien być poprawny"


class TestInitialState:
    def test_board_is_empty_at_start(self, game):
        assert game.get_board() == [TicTacToe.EMPTY] * 9

    def test_x_starts_first(self, game):
        assert game.current_player == TicTacToe.PLAYER_X

    def test_no_winner_at_start(self, game):
        assert game.winner is None
        assert not game.is_game_over()
        assert not game.is_draw()

    def test_initial_status_message(self, game):
        assert game.status() == "Ruch gracza: X"


class TestMoves:
    def test_valid_move_places_mark(self, game):
        assert game.make_move(0) is True
        assert game.get_board()[0] == TicTacToe.PLAYER_X

    def test_players_alternate(self, game):
        play(game, [0, 1, 2])
        board = game.get_board()
        assert board[0] == TicTacToe.PLAYER_X
        assert board[1] == TicTacToe.PLAYER_O
        assert board[2] == TicTacToe.PLAYER_X
        assert game.current_player == TicTacToe.PLAYER_O

    def test_cannot_play_on_occupied_cell(self, game):
        game.make_move(4)
        assert game.make_move(4) is False
        assert game.current_player == TicTacToe.PLAYER_O

    @pytest.mark.parametrize("index", [-1, 9, 100])
    def test_rejects_out_of_range_index(self, game, index):
        assert game.make_move(index) is False
        assert game.current_player == TicTacToe.PLAYER_X

    def test_rejects_moves_after_game_over(self, game):
        play(game, [0, 3, 1, 4, 2])  # X wygrywa górnym wierszem
        assert game.is_game_over()
        assert game.make_move(8) is False
        assert game.get_board()[8] == TicTacToe.EMPTY


class TestWinning:
    @pytest.mark.parametrize("line,moves", [
        ((0, 1, 2), [0, 3, 1, 4, 2]),  # górny wiersz
        ((3, 4, 5), [3, 0, 4, 1, 5]),  # środkowy wiersz
        ((6, 7, 8), [6, 0, 7, 1, 8]),  # dolny wiersz
        ((0, 3, 6), [0, 1, 3, 4, 6]),  # lewa kolumna
        ((1, 4, 7), [1, 0, 4, 2, 7]),  # środkowa kolumna
        ((2, 5, 8), [2, 0, 5, 1, 8]),  # prawa kolumna
        ((0, 4, 8), [0, 1, 4, 2, 8]),  # przekątna główna
        ((2, 4, 6), [2, 0, 4, 1, 6]),  # przekątna przeciwna
    ])
    def test_x_wins_each_line(self, game, line, moves):
        play(game, moves)
        assert game.winner == TicTacToe.PLAYER_X
        assert game.winning_line == line
        assert game.is_game_over()
        assert game.status() == "Wygrał gracz X!"

    def test_o_can_win(self, game):
        play(game, [0, 3, 1, 4, 8, 5])  # O zdobywa środkowy wiersz
        assert game.winner == TicTacToe.PLAYER_O
        assert game.status() == "Wygrał gracz O!"

    def test_player_does_not_switch_after_winning_move(self, game):
        play(game, [0, 3, 1, 4, 2])
        assert game.current_player == TicTacToe.PLAYER_X


class TestDraw:
    def test_full_board_without_winner_is_draw(self, game):
        # X O X
        # X O O
        # O X X
        play(game, [0, 1, 2, 4, 3, 5, 7, 6, 8])
        assert game.is_draw()
        assert game.winner is None
        assert game.is_game_over()
        assert game.status() == "Remis!"

    def test_win_takes_precedence_over_draw(self, game):
        play(game, [0, 3, 1, 4, 2])
        assert not game.is_draw()
        assert game.winner == TicTacToe.PLAYER_X


class TestReset:
    def test_reset_restores_initial_state(self, game):
        play(game, [0, 3, 1, 4, 2])
        assert game.is_game_over()
        game.reset()
        assert game.get_board() == [TicTacToe.EMPTY] * 9
        assert game.current_player == TicTacToe.PLAYER_X
        assert game.winner is None
        assert game.winning_line is None
        assert not game.is_game_over()

    def test_can_play_after_reset(self, game):
        play(game, [0, 3, 1, 4, 2])
        game.reset()
        assert game.make_move(4) is True
        assert game.get_board()[4] == TicTacToe.PLAYER_X


class TestBoardEncapsulation:
    def test_get_board_returns_copy(self, game):
        board = game.get_board()
        board[0] = TicTacToe.PLAYER_X
        assert game.get_board()[0] == TicTacToe.EMPTY
