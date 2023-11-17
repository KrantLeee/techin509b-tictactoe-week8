import unittest
from logic import GameBoard
from cli import TicTacToeGame, TicTacToeAI

class TestTicTacToe(unittest.TestCase):

    def test_initialization_empty_board(self):
        board = GameBoard()
        for row in board.board:
            for cell in row:
                self.assertIsNone(cell)

    def test_game_initialization_mode(self):
        board = GameBoard()
        game_1 = TicTacToeGame(board, "1")  # single-player
        game_2 = TicTacToeGame(board, "2")  # two-player
        self.assertEqual(game_1.mode, "1")
        self.assertEqual(game_2.mode, "2")

    def test_player_assignment(self):
        board = GameBoard()
        game = TicTacToeGame(board, "2")
        self.assertEqual(game.current_player, 'X')

    def test_switch_player(self):
        board = GameBoard()
        game = TicTacToeGame(board, "2")
        game.switch_player()
        self.assertEqual(game.current_player, 'O')

    def test_win_condition(self):
        board = GameBoard()
        game = TicTacToeGame(board, "2")
        # Simulate a win condition
        game.board.set_cell(0, 0, 'X')
        game.board.set_cell(1, 1, 'X')
        game.board.set_cell(2, 2, 'X')
        self.assertTrue(game.board.check_winner('X'))

    def test_draw_condition(self):
        board = GameBoard()
        game = TicTacToeGame(board, "2")
        # Simulate a draw
        for i in range(3):
            for j in range(3):
                game.board.set_cell(i, j, 'X' if (i + j) % 2 == 0 else 'O')
        self.assertTrue(game.board.check_draw())

    def test_play_on_viable_spot(self):
        board = GameBoard()
        board.set_cell(0, 0, 'X')
        self.assertIsNotNone(board.get_cell(0, 0))
        self.assertIsNone(board.get_cell(1, 1))  

    def test_correct_winner_detected(self):
        game = GameBoard()
        game.board = [
            ['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(game.check_winner('X'), 'X')

if __name__ == '__main__':
    unittest.main()
