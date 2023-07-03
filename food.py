import pyglet
import random
from position import Position


class Food:
    def __init__(self, position, offset_x, offset_y, box_size, board_width, board_height):
        self.position = position
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.box_size = box_size
        self.board_width = board_width
        self.board_height = board_height

        self.circle = pyglet.shapes.Circle(
            x=self.position.x * self.box_size + self.offset_x + (self.box_size // 2),
            y=self.position.y * self.box_size + self.offset_y + (self.box_size // 2),
            radius=self.box_size / 3,
            color=(255, 0, 0))

    def random_reposition(self, occupied_positions):
        possible_positions = [i for i in range(0, self.board_width * self.board_height)]
        for pos in occupied_positions:
            possible_positions.remove(pos.y * self.board_width + pos.x)
        picked_position = random.choice(possible_positions)
        self.position = Position(picked_position % self.board_width, picked_position // self.board_width)
        self.circle.x = self.position.x * self.box_size + self.offset_x + (self.box_size // 2)
        self.circle.y = self.position.y * self.box_size + self.offset_y + (self.box_size // 2)

    def draw(self):
        self.circle.draw()