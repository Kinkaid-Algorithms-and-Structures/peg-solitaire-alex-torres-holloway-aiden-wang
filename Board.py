import Peg
class Board:

    def __init__(self):
        self.board = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.board_labels = [["A"], ["B", "C"], ["D", "E", "F"], ["G", "H", "I", "J"], ["K", "L", "M", "N", "O"]]

    def create_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = Peg(i, j)

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == -1:
                    print("o")
                else:
                    print("+")

    def game_over(self):
        pass

    def





