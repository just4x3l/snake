import pyglet

from fillable_square import FillableSquare
from snake import Snake
from direction import Direction
from position import Position
from food import Food


class Board:
    def __init__(self, width, height, box_size, board_offset_x, board_offset_y, outside_border_width, initial_snake_positions, initial_snake_direction):
        self.width = width
        self.height = height
        self.box_size = box_size
        self.offset_x = board_offset_x + outside_border_width
        self.offset_y = board_offset_y + outside_border_width
        self.squares = []
        self.batch = None
        self.initialize_board()

        self.border = pyglet.shapes.Rectangle(board_offset_x, board_offset_y,
                                              self.width * self.box_size + 2 * outside_border_width,
                                              self.height * self.box_size + 2 * outside_border_width,
                                              color=(50, 50, 50))

        self.snake = Snake(board_width=width, board_height=height,
                           initial_positions=initial_snake_positions,
                           initial_direction=initial_snake_direction)

        self.initial_food_position = Position(0, 0)
        self.food = Food(self.initial_food_position, self.offset_x, self.offset_y, self.box_size, self.width,
                         self.height)
        self.food.random_reposition(self.snake.positions)

    def initialize_board(self):
        self.batch = pyglet.graphics.Batch()
        self.squares = [
            FillableSquare(x=i, y=j,
                           side=self.box_size,
                           filled=False,
                           batch=self.batch,
                           offset_x=self.offset_x, offset_y=self.offset_y)
            for i in range(self.width)
            for j in range(self.height)
        ]

    def draw(self):
        self.border.draw()
        self.snake.move()
        self.batch.draw()
        self.food.draw()

    def change_snake_direction(self, direction: Direction):
        self.snake.change_direction(direction)

    def update(self):
        if self.snake.alive():
            for pos in self.snake.positions:
                self.squares[pos.x * self.height + pos.y].fill()
            for pos in self.snake.disappear:
                self.squares[pos.x * self.height + pos.y].empty()

            if self.snake.can_eat(self.food.position):
                self.food.random_reposition(self.snake.positions)
                return 1
            else:
                return 0
        else:
            exit()
        return 0
