from math import floor
import random
from Peg import Peg

class Board:

    def __init__(self):
        self.board = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]

    def create_board(self) -> None:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = Peg(i, j)
        row = random.randint(0, len(self.board)-1)
        col = random.randint(0, len(self.board[row])-1)
        self.board[row][col] = -1

    def print_board(self) -> None:
        for i in range(len(self.board)):
            print("")
            print(f"{i}  ", end='')
            for k in range(4-i):
                print("_", end='')
            for j in range(len(self.board[i])):
                if self.board[i][j] == -1:
                    print("o", end='')
                else:
                    print("+", end='')
                if not j == len(self.board[i])-1:
                    print("_", end='')
            for k in range(4-i):
                print("_", end='')

    def is_legal_move(self, current_pos: Peg, target_pos: Peg) -> bool:
        current_index = None
        target_index = None
        print(current_index, target_index)

    def move(self, current_pos: Peg, target_pos: Peg) -> None:
        init_pos = current_pos.get_pos()
        final_pos = target_pos.get_pos()
        self.board[final_pos[0]][final_pos[1]] = self.board[init_pos[0]][init_pos[1]]
        self.board[init_pos[0]][init_pos[1]] = -1
        self.board[final_pos[0]][final_pos[1]].update_pos(final_pos[0], final_pos[1])

    def remove(self, current_pos: Peg, target_pos: Peg) -> None:
        pass

    def get_peg_count(self) -> int:
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if not self.board[i][j] == -1:
                    count +1
        return count

    def each_has_neighbors(self) -> bool:
        #call check if has neighbors in each peg
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.in_bounds(str(i - 1), str(j - 1)) and not self.board[i - 1][j - 1] == -1:
                    return True
                if self.in_bounds(str(i - 1), str(j + 1)) and not self.board[i - 1][j + 1] == -1:
                    return True
                if self.in_bounds(str(i), str(j - 1)) and not self.board[i][j - 1] == -1:
                    return True
                if self.in_bounds(str(i), str(j + 1)) and not self.board[i][j + 1] == -1:
                    return True
                if self.in_bounds(str(i + 1), str(j - 1)) and not self.board[i + 1][j - 1] == -1:
                    return True
                if self.in_bounds(str(i + 1), str(j + 1)) and not self.board[i + 1][j + 1] == -1:
                    return True

        return False
    
    def get_peg(self, i: str, j: str) -> Peg:
        return self.board[int(i)][int(j)]

    def in_bounds(self, i: str, j:str) -> bool:
        if int(i) < len(self.board) and int(j) < len(self.board[int(i)]):
            return True





