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
        self.board[row][col].set_empty(True)

    def print_board(self) -> None:
        for i in range(len(self.board)):
            print("")
            print(f"{i}  ", end='')
            for k in range(4-i):
                print("_", end='')
            for j in range(len(self.board[i])):
                if self.board[i][j].is_empty():
                    print("o", end='')
                else:
                    print("+", end='')
                if not j == len(self.board[i])-1:
                    print("_", end='')
            for k in range(4-i):
                print("_", end='')

    def is_legal_move(self, current_peg: Peg, target_peg: Peg) -> bool:
        init_pos = current_peg.get_pos()
        final_pos = target_peg.get_pos()
        if self.board[init_pos[0]][init_pos[1]].is_empty():
            return False
        if not self.board[final_pos[0]][final_pos[1]].is_empty():
            return False
        if final_pos[0] == init_pos[0] + 2:
            if not (final_pos[1] == init_pos[1] or final_pos[1] == init_pos[1] + 2):
                return False
            elif final_pos[1] == init_pos[1]:
                if self.board[init_pos[0]+1][init_pos[1]].is_empty():
                    return False
            elif final_pos[1] == init_pos[1] + 2:
                if self.board[init_pos[0]+1][init_pos[1]+1].is_empty():
                    return False
        if final_pos[0] == init_pos[0] - 2:
            if not (final_pos[1] == init_pos[1] or final_pos[1] == init_pos[1] - 2):
                return False
            elif final_pos[1] == init_pos[1]:
                if self.board[init_pos[0]-1][init_pos[1]].is_empty():
                    return False
            elif final_pos[1] == init_pos[1] - 2:
                if self.board[init_pos[0]-1][init_pos[1]-1].is_empty():
                    return False
        if final_pos[0] == init_pos[0]:
            if not (final_pos[1] == init_pos[1] + 2 or final_pos[1] == init_pos[1] - 2):
                return False
            elif final_pos[1] == init_pos[1] + 2:
                if self.board[init_pos[0]][init_pos[1]+1].is_empty():
                    return False
            elif final_pos[1] == init_pos[1] - 2:
                if self.board[init_pos[0]][init_pos[1]-1].is_empty():
                    return False
        if not (final_pos[0] == init_pos[0] or final_pos[0] == init_pos[0] + 2 or final_pos[0] == init_pos[0] - 2):
            return False
        return True


    def move(self, current_peg: Peg, target_peg: Peg) -> None:
        init_pos = current_peg.get_pos()
        final_pos = target_peg.get_pos()
        self.board[init_pos[0]][init_pos[1]].set_empty(True)
        self.board[final_pos[0]][final_pos[1]].set_empty(False)

    def remove(self, current_peg: Peg, target_peg: Peg) -> None:
        init_pos = current_peg.get_pos()
        final_pos = target_peg.get_pos()
        if abs(init_pos[1] - final_pos[1]) == 2:
            self.board[(init_pos[0] + final_pos[0]) // 2][(init_pos[1] + final_pos[1]) // 2].set_empty(True)
        if init_pos[1] == final_pos[1]:
            self.board[(init_pos[0] + final_pos[0]) // 2][(init_pos[1] + final_pos[1]) // 2].set_empty(True)
        if init_pos[0] == final_pos[0]:
            self.board[(init_pos[0] + final_pos[0]) // 2][(init_pos[1] + final_pos[1]) // 2].set_empty(True)

    def get_peg_count(self) -> int:
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if not self.board[i][j].is_empty():
                    count += 1
        return count

    def has_legal_moves(self) -> bool:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j].is_empty():
                    continue
                if self.in_bounds(str(i+2), str(j)):
                    if self.is_legal_move(self.board[i][j], self.board[i+2][j]):
                        return True
                if self.in_bounds(str(i+2), str(j+2)):
                    if self.is_legal_move(self.board[i][j], self.board[i+2][j+2]):
                        return True
                if self.in_bounds(str(i-2), str(j)):
                    if self.is_legal_move(self.board[i][j], self.board[i-2][j]):
                        return True
                if self.in_bounds(str(i-2), str(j-2)):
                    if self.is_legal_move(self.board[i][j], self.board[i-2][j-2]):
                        return True
                if self.in_bounds(str(i), str(j-2)):
                    if self.is_legal_move(self.board[i][j], self.board[i][j-2]):
                        return True
                if self.in_bounds(str(i), str(j+2)):
                    if self.is_legal_move(self.board[i][j], self.board[i][j+2]):
                        return True
        return False
    
    def get_peg(self, i: str, j: str) -> Peg:
        return self.board[int(i)][int(j)]

    def in_bounds(self, i: str, j:str) -> bool:
        if len(self.board) > int(i) >= 0 and len(self.board[int(i)]) > int(j) >= 0:
            return True
        return False





