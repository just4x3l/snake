import pyglet

from game_window import GameWindow
from position import Position
from direction import Direction

config = {
    "board_offset_x": 20,
    "board_offset_y": 20,
    "outside_border_width": 10,

    "rows": 15,
    "columns": 20,
    "box_size": 30,

    "initial_snake_positions": [Position(0, 0), Position(1, 0)],
    "initial_snake_direction": Direction.RIGHT
}

if __name__ == '__main__':
    window = GameWindow(config)
    pyglet.app.run(1/10)
