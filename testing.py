from tictactoe import actions
from tictactoe import minimax
from tictactoe import result
import unittest



X = "X"
O = "O"
EMPTY = None


class Test_minimax(unittest.TestCase):

    def test_actions(self):
        board = [[X,X,O], [EMPTY, EMPTY, O], [EMPTY, EMPTY, EMPTY]]
        result = {(1,0),(2,0),(1,1),(2,1),(2,2)}
        self.assertEqual(result, actions(board))

    def test_result(self):
        board = [[X, X, O], [EMPTY, EMPTY, O], [EMPTY, EMPTY, EMPTY]]
        res = [[X, X, O], [EMPTY, EMPTY, O], [EMPTY, EMPTY, X]]
        self.assertEqual(result(board, (2,2)), res)











if __name__ == '__main__':
    unittest.main()