
class GameBoard:
    def __init__(self):
        self.board = [[None for i in range(3)] for j in range(3)]
        self.winner = None
    
    def get_cell(self, x, y):
        return self.board[x][y]
    
    def set_cell(self, x, y, value):
        self.board[x][y] = value

    def check_winner(self, player):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""  
        # Check rows, columns, and diagonals
        board = self.board
        winning = any(
            (board[i][0] == board[i][1] == board[i][2] == player) or  # rows
            (board[0][i] == board[1][i] == board[2][i] == player) or  # columns
            (board[0][0] == board[1][1] == board[2][2] == player) or  # top-left to bottom-right diagonal
            (board[0][2] == board[1][1] == board[2][0] == player)    # top-right to bottom-left diagonal
            for i in range(3)
        )
        return player if winning else None

    def check_draw(self):
        return all(cell is not None for row in self.board for cell in row)


   

