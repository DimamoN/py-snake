import time
from random import random


class Engine:

    def __init__(self, root, canvas, game_map, snake, lb_start_game):
        self.root = root
        self.canvas = canvas
        self.game_map = game_map
        self.in_game = True
        self.turn_time = 0.2
        self.lb_start_game = lb_start_game
        self.snake = snake

        # food
        self.spawn_threshold = 10
        self.spawn_turns = 0
        self.food_pos_list = []

    def set_start_food(self, food_pos_list):
        self.food_pos_list = food_pos_list

    def start_stop(self, event):
        self.in_game = not self.in_game

    def game_loop(self, event):
        self.lb_start_game.destroy()

        while self.in_game:
            self.root.update()
            self.root.update_idletasks()

            time.sleep(self.turn_time)

            if self.should_spawn_food():
                pos = self.game_map.generate_new_food_pos()
                self.food_pos_list.append(pos)
                self.spawn_turns = 0


            self.snake.move()

            self.canvas.delete('all')
            self.game_map.render_grid(self.canvas)
            self.game_map.render_food(self.canvas, self.food_pos_list)
            self.game_map.render_snake(self.canvas, self.snake)

            self.spawn_turns += 1
            print("test")

    def should_spawn_food(self):
        return self.spawn_turns >= self.spawn_threshold
