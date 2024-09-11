from Peg import Peg
import random
class Board:
    def __init__(self):
        self.board = []
        self.num_row = 5
        self.game_running = True
    def create_board(self):
        pegs = []
        for i in range(self.num_row):
            row = []
            for j in range(i+1):
                peg = Peg(i,j,True)
                row.append(peg)
                pegs.append(peg)
            self.board.append(row)
        random_peg = random.choice(pegs)
        random_peg.alive = False
        print(random_peg)
    def legal_moves(self):
        moves = ((-2,2), (0,2), (2,2),
                 (-2,0), (0,0), (2,0),
                 (-2,-2), (0,-2),(2,-2))
        for i in range(self.num_row):
            for j in range(i+1):
                if not self.board[i][j].is_alive():
                    for k in range(len(moves)):
                        if self.board[i+moves[k][0]][j+moves[k][1]] >= 0 or self.board[i+moves[k][0]][j+moves[k][1]] <=
    def is_legal(self):
        pass
    def print_board(self):
        print("---------")
        spaces = " "
        num_spaces = 4
        for i in range(self.num_row):
            print_row = ""
            print_row += spaces * num_spaces
            for j in range(i+1):
                if not self.board[i][j].is_alive():
                    print_row += "O"
                    if j < 0 or j < i:
                        print_row+="-"
                else:
                    print_row += "T"
                    if j < 0 or j < i:
                        print_row+="-"
            print_row += spaces * num_spaces
            num_spaces -= 1
            print(print_row)
        print("---------")

    def game_loop(self):
        pass






