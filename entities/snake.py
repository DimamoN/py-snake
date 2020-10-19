from enum import Enum

from entities.pos import Pos


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class Snake:

    def __init__(self, start_pos):
        self.body = start_pos
        self.direction = Direction.RIGHT


    # def change_direction(self, event):
    #     if event.keysym == 'w' and self.direction != Direction.DOWN:
    #         self.direction = Direction.UP
    #     elif event.keysym == 's' and self.direction != Direction.UP:
    #         self.direction = Direction.DOWN
    #     elif event.keysym == 'a' and self.direction != Direction.RIGHT:
    #         self.direction = Direction.LEFT
    #     elif event.keysym == 'd' and self.direction != Direction.LEFT:
    #         self.direction = Direction.RIGHT
    #     else:
    #         raise Exception("unsupported")


    def move(self, event):
        print("- Moving")
        head_cell = Pos.fromPos(self.body[0])
        print("head_cell:" + str(head_cell))

        if event.keysym == 'w' and self.direction != Direction.DOWN:
            self.direction = Direction.UP
            head_cell.y -= 1
        elif event.keysym == 's' and self.direction != Direction.UP:
            self.direction = Direction.DOWN
            head_cell.y += 1
        elif event.keysym == 'a' and self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT
            head_cell.x -= 1
        elif event.keysym == 'd' and self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT
            head_cell.x += 1
        else:
            raise Exception("unsupported")

        print("direction:" + self.direction.name)
        print("new head_cell:" + str(head_cell))
        self.body.insert(0, head_cell)

        self.body.remove(self.body[-1])

    def count(self):
        return len(self.body)

    def head_pos(self):
        return self.body[0]
