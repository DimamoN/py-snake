import tkinter
import time

from entities.engine import Engine
from entities.map import Map
from entities.pos import Pos
from entities.snake import Snake

ROOT_SIZE = "640x640"

CANV_WIDTH = 640
CANV_HEIGHT = 640
ROOT_BG = "black"
GAME_TITLE = "game"

MAP_SIZE_X = 20
MAP_SIZE_Y = 20
CELL_SIZE = 32

def root():
    root = tkinter.Tk()
    root.resizable(width=False, height=False)
    root.geometry(ROOT_SIZE)
    root.title(GAME_TITLE)
    root['bg'] = ROOT_BG

    canvas = tkinter.Canvas(root, width=CANV_WIDTH, height=CANV_HEIGHT)
    canvas.pack()

    game_map = Map(MAP_SIZE_X, MAP_SIZE_Y, CELL_SIZE)

    lb = tkinter.Label(canvas, text="Press Enter to Start the game", bg="white")
    lb.place(x=300, y=100)

    snake = Snake([Pos(4, 1), Pos(3, 1), Pos(2, 1), Pos(1, 1)])
    engine = Engine(root, canvas, game_map, snake, lb)
    engine.set_start_food([Pos(10, 10), Pos(8, 5)])

    root.bind('<space>', engine.start_stop)
    root.bind('<Return>', engine.game_loop)

    root.bind('<w>', snake.move)
    root.bind('<a>', snake.move)
    root.bind('<s>', snake.move)
    root.bind('<d>', snake.move)

    root.mainloop()


if __name__ == '__main__':
    root()
