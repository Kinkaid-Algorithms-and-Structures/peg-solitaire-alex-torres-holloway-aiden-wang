class Peg:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.empty = False

    def get_pos(self) -> list:
        return [self.x, self.y]

    def update_pos(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def is_empty(self) -> bool:
        return self.empty

    def set_empty(self, emp: bool) -> bool:
        self.empty = emp
