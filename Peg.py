class Peg:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_pos(self) -> list:
        return [self.x, self.y]

    def has_neighbors(self) -> bool:
        pass