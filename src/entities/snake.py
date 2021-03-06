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
        self.direction_changed_in_that_turn = False

    def change_direction(self, event):
        if not self.direction_changed_in_that_turn:
            if event.keysym == 'w' and self.direction != Direction.DOWN:
                self.direction = Direction.UP
            elif event.keysym == 's' and self.direction != Direction.UP:
                self.direction = Direction.DOWN
            elif event.keysym == 'a' and self.direction != Direction.RIGHT:
                self.direction = Direction.LEFT
            elif event.keysym == 'd' and self.direction != Direction.LEFT:
                self.direction = Direction.RIGHT
            else:
                raise Exception("unsupported")
            self.direction_changed_in_that_turn = True

    def next_pos(self):
        head_cell = Pos.fromPos(self.body[0])
        if self.direction == Direction.UP:
            head_cell.y -= 1
        elif self.direction == Direction.DOWN:
            head_cell.y += 1
        elif self.direction == Direction.LEFT:
            head_cell.x -= 1
        elif self.direction == Direction.RIGHT:
            head_cell.x += 1
        return head_cell

    def move(self, should_grow):
        print("- Moving")
        head_cell = Pos.fromPos(self.body[0])
        print("head_cell:" + str(head_cell))

        if self.direction == Direction.UP:
            head_cell.y -= 1
        elif self.direction == Direction.DOWN:
            head_cell.y += 1
        elif self.direction == Direction.LEFT:
            head_cell.x -= 1
        elif self.direction == Direction.RIGHT:
            head_cell.x += 1

        print("direction:" + self.direction.name)
        print("new head_cell:" + str(head_cell))
        self.body.insert(0, head_cell)

        if not should_grow:
            self.body.remove(self.body[-1])

        self.direction_changed_in_that_turn = False


