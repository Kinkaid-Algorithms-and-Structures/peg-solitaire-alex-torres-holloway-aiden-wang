from Peg import Peg
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
            print(self.board)

    def legal_move(self):
        pass







