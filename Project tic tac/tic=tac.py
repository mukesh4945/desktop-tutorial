class TicTacToe:
    """
    Class to represent a Tic-Tac-Toe game.
    """

    def __init__(self):
        """
        Initializes the game board with empty spaces.
        """
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        """
        Prints the current state of the game board.
        """
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        """
        Makes a move on the board.

        Args:
            row (int): The row index of the move.
            col (int): The column index of the move.

        Returns:
            bool: True if the move is valid and made, False otherwise.
        """
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid move: Row and column must be between 0 and 2.")
            return False
        if self.board[row][col] != " ":
            print("Invalid move: The cell is already occupied.")
            return False

        self.board[row][col] = self.current_player
        # Switch the player
        self.current_player = "O" if self.current_player == "X" else "X"
        return True

    def check_win(self):
        """
        Checks if a player has won the game.

        Returns:
            str: "X" or "O" if a player has won, None otherwise.
        """
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != " ":
                return self.board[0][col]

        # Check diagonals
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2]
            and self.board[0][0] != " "
        ):
            return self.board[0][0]
        if (
            self.board[0][2] == self.board[1][1] == self.board[2][0]
            and self.board[0][2] != " "
        ):
            return self.board[0][2]

        return None

    def is_board_full(self):
        """
        Checks if the game board is full.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def play_game(self):
        """
        Plays a game of Tic-Tac-Toe.
        """
        while True:
            self.print_board()

            try:
                row = int(input(f"Player {self.current_player}, enter row (0-2): "))
                col = int(input(f"Player {self.current_player}, enter column (0-2): "))
            except ValueError:
                print("Invalid input: Please enter integers between 0 and 2.")
                continue

            if not self.make_move(row, col):
                continue

            winner = self.check_win()
            if winner:
                self.print_board()
                print(f"Player {winner} wins!")
                break

            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
