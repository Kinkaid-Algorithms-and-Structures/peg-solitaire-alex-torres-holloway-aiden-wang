from Peg import Peg
import random
class Board:
    def __init__(self):
        self.board = []
        self.num_row = 5
    def create_board(self):
        for i in range(self.num_row):
            row = []
            for j in range(i+1):
                peg = Peg(i,j)
                row.append(peg)
            self.board.append(row)

    def legal_move(self):
        pass







