from Peg import Peg
class Board:

    def __init__(self):
        self.board = [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.board_labels = [["A"], ["B", "C"], ["D", "E", "F"], ["G", "H", "I", "J"], ["K", "L", "M", "N", "O"]]

    def create_board(self) -> None:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = Peg(i, j)

    def print_board(self) -> None:
        for i in range(len(self.board)):
            print("")
            for j in range(len(self.board[i])):
                if self.board[i][j] == -1:
                    print("o", end='')
                else:
                    print("+", end='')

    def is_legal_move(self, current_pos: int, target_pos: int) -> bool:
        current_index = None
        target_index = None
        print(current_index, target_index)

    def move(self, current_pos: int, target_pos: int) -> None:
        pass

    def get_peg_count(self) -> int:
        #test
        pass

    def each_has_neighbors(self) -> bool:
        #call check if has neighbors in each peg
        pass






