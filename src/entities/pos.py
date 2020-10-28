
class Pos:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def fromPos(cls, pos):
        return Pos(pos.x, pos.y)

    def __str__(self):
        return "Pos(x=" + str(self.x) + ", y=" + str(self.y) + ")"

    def __eq__(self, other):
        if isinstance(other, Pos):
            return self.x == other.x and self.y == other.y
        return False
