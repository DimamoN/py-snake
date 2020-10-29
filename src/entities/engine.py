import time
import config

from utils.sound import play_sound_pop, play_sound_hit


class Engine:

    def __init__(self, root, canvas, game_map, snake, lb_start_game):
        self.root = root
        self.canvas = canvas
        self.game_map = game_map
        self.in_game = True
        self.turn_time = config.TURN_TIME
        self.lb_start_game = lb_start_game
        self.snake = snake

        # food
        self.spawn_threshold = config.SPAWN_THRESHOLD
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

            # food
            if self.should_spawn_food():
                pos = self.game_map.generate_new_food_pos()
                self.food_pos_list.append(pos)
                self.spawn_turns = 0

            snake_should_grow = False
            next_snake_pos = self.snake.next_pos()

            if next_snake_pos in self.snake.body:
                print('SELF HIT ON: ' + str(next_snake_pos))
                self.in_game = False
                play_sound_hit()
                continue

            # Check moving outside the map
            if self.__is_out_of_map(next_snake_pos):
                print('OUT OF MAP: ' + str(next_snake_pos))
                self.in_game = False
                play_sound_hit()
                continue

            if next_snake_pos in self.food_pos_list:
                snake_should_grow = True
                play_sound_pop()
                self.food_pos_list.remove(next_snake_pos)

            self.snake.move(snake_should_grow)

            # render
            self.canvas.delete('all')
            self.game_map.render_grid(self.canvas)
            self.game_map.render_food(self.canvas, self.food_pos_list)
            self.game_map.render_snake(self.canvas, self.snake)

            self.spawn_turns += 1

    def __is_out_of_map(self, next_pos):
        return next_pos.x < 0 or next_pos.y < 0 \
               or next_pos.x > config.MAP_SIZE_X \
               or next_pos.y > config.MAP_SIZE_Y

    def should_spawn_food(self):
        return self.spawn_turns >= self.spawn_threshold
