# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import random
from logic import GameBoard

class TicTacToeGame:
    def __init__(self, board, mode):
        self.board = board
        self.mode = mode  # 1 for single-player, 2 for two-player
        self.current_player = 'X'

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_turn(self, x, y):
        self.board.set_cell(x, y, self.current_player)
        winner = self.board.check_winner(self.current_player)
        if winner:
            self.board.winner = winner
            return True
        self.switch_player()
        return False

class TicTacToeAI:
    def __init__(self, board):
        self.board = board

    def get_ai_move(self):
        empty_cells = [(a, b) for a in range(3) for b in range(3) if self.board.get_cell(a, b) is None]
        return random.choice(empty_cells)

class UserInterface:
    def __init__(self, game, ai=None):
        self.game = game
        self.ai = ai
        
    def display_board(self):
        for row in self.game.board.board:
            print(' | '.join([' ' if cell is None else cell for cell in row]))
            print('-' * 9)

    def get_user_move(self):
        while True:
            user_input = input('Please make your movement by typing x,y (e.g., 1,2):').split(',')
            if len(user_input) == 2 and user_input[0].isdigit() and user_input[1].isdigit(): # Check if the input is legal
                x, y = int(user_input[0]), int(user_input[1])
                if 0 <= x <= 2 and 0 <= y <= 2: # Check if the input is within boundary
                    if self.game.board.get_cell(x, y) is None:  # Check if the position is empty
                        return x, y
                    else:
                        print("This position is already taken. Please choose another one.")
                else:
                    print("Invalid coordinates. Please enter values between 0 and 2.")
            else:
                print("Invalid input. Please enter in the format x,y.")

        
    def play_game(self):
        while True:
            self.display_board()
            print(f"·It's {self.game.current_player}'s turn·")
            if self.game.mode == '1' and self.game.current_player == 'O':
                x, y = self.ai.get_ai_move()
            else:
                x, y = self.get_user_move()

            if self.game.play_turn(x, y):
                self.display_board()
                print(f"Player {self.game.board.winner} wins!")
                break

            if self.game.board.check_draw():
                self.display_board()
                print("It's a draw!")
                break



def start_game():
    board = GameBoard()
    mode = input("Choose a mode (1 for single-player, 2 for two-player): ")
    while mode not in ['1', '2']:
        print("Invalid mode. Please enter 1 or 2.")
        mode = input("Choose a mode (1 for single-player, 2 for two-player): ")

    game = TicTacToeGame(board, mode)
    ai = TicTacToeAI(game.board) if mode == '1' else None
    ui = UserInterface(game, ai)
    ui.play_game()

if __name__ == '__main__':
    start_game()