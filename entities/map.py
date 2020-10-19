SPAWN_THRESHOLD = 10


class Map:

    def __init__(self, size_x, size_y, cell_size):
        self.size_x = size_x
        self.size_y = size_y
        self.cell_size = cell_size

    def render_grid(self, canvas):
        for x in range(self.size_x):
            for y in range(self.size_y):
                # x -----> size_x
                canvas.create_line(x * self.cell_size, y * self.cell_size,
                                   self.size_x * self.cell_size, y * self.cell_size, fill="black")
                # y -----> size_y
                canvas.create_line(x * self.cell_size, y * self.cell_size,
                                   x * self.cell_size, self.size_y * self.cell_size, fill="black")

    def render_food(self, canvas, food_pos_list):
        for pos in food_pos_list:
            coord_x_1 = (pos.x * self.cell_size) - self.cell_size
            coord_y_1 = (pos.y * self.cell_size) - self.cell_size
            coord_x_2 = (pos.x * self.cell_size)
            coord_y_2 = (pos.y * self.cell_size)
            canvas.create_rectangle(coord_x_1, coord_y_1, coord_x_2, coord_y_2, fill="green")

    def render_snake(self, canvas, snake):
        for pos in snake.body:
            coord_x_1 = (pos.x * self.cell_size) - self.cell_size
            coord_y_1 = (pos.y * self.cell_size) - self.cell_size
            coord_x_2 = (pos.x * self.cell_size)
            coord_y_2 = (pos.y * self.cell_size)
            canvas.create_rectangle(coord_x_1, coord_y_1, coord_x_2, coord_y_2, fill="red")
