class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, p):
        return Position(self.x + p.x, self.y + p.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) + hash(self.y)