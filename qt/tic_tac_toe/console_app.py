from logic import TicTacToe


def render_board(game):
    board = game.get_board()
    rows = []
    for r in range(3):
        cells = []
        for c in range(3):
            i = r * 3 + c
            cells.append(board[i] if board[i] != TicTacToe.EMPTY else str(i))
        rows.append(" " + " | ".join(cells) + " ")
    return ("\n" + "-" * 13 + "\n").join(rows)


def prompt_move(game):
    while True:
        raw = input(f"{game.status()} - podaj numer pola (0-8) lub 'q' aby zakończyć: ").strip()
        if raw.lower() == "q":
            return None
        if not raw.isdigit():
            print("Nieprawidłowe wejście.")
            continue
        index = int(raw)
        if not game.make_move(index):
            print("Ruch niedozwolony, spróbuj ponownie.")
            continue
        return index


def main():
    game = TicTacToe()
    print("Kółko i krzyżyk - wersja konsolowa")

    while True:
        print()
        print(render_board(game))
        if game.is_game_over():
            print()
            print(game.status())
            again = input("Zagrać jeszcze raz? (t/n): ").strip().lower()
            if again == "t":
                game.reset()
                continue
            print("Do zobaczenia!")
            break
        if prompt_move(game) is None:
            print("Do zobaczenia!")
            break


if __name__ == "__main__":
    main()
