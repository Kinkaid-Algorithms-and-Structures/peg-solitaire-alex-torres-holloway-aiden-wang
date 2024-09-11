class Peg:
    def __init__(self, x, y, alive):
        self.x = x
        self.y = y
        self.alive = True

    def get_pos(self):
        return self.x, self.y
    def is_alive(self):
        return self.alive
