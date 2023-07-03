import pyglet
from board import Board
from pyglet.window import key
from direction import Direction


class GameWindow(pyglet.window.Window):
    def __init__(self, config):
        super().__init__(caption="Snake Game",
                         width=config["columns"] * config["box_size"] + 200,
                         height=config["rows"] * config["box_size"] + 100)

        self.title_label = pyglet.text.Label("Snake",
                                             font_name="Times New Roman",
                                             font_size=28,
                                             x=config["board_offset_x"], y=self.height - 10,
                                             anchor_x="left", anchor_y="top")

        self.score = 0
        self.score_label = pyglet.text.Label('Score: 0',
                                             font_name='Times New Roman',
                                             font_size=20,
                                             x=self.width - 20, y=config["board_offset_y"],
                                             anchor_x='right', anchor_y='bottom')

        self.background = pyglet.shapes.Rectangle(0, 0, self.width, self.height, color=(100, 100, 100))

        self.board = Board(width=config["columns"], height=config["rows"],
                           box_size=config["box_size"],
                           board_offset_x=config["board_offset_x"], board_offset_y=config["board_offset_y"],
                           outside_border_width=config["outside_border_width"],
                           initial_snake_positions=config["initial_snake_positions"],
                           initial_snake_direction=config["initial_snake_direction"])

    def on_draw(self):
        self.clear()
        self.background.draw()
        self.title_label.draw()
        self.score += self.board.update()
        self.score_label.text = "Score: " + str(self.score)
        self.score_label.draw()
        self.board.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.board.change_snake_direction(Direction.UP)
        elif symbol == key.RIGHT:
            self.board.change_snake_direction(Direction.RIGHT)
        elif symbol == key.DOWN:
            self.board.change_snake_direction(Direction.DOWN)
        elif symbol == key.LEFT:
            self.board.change_snake_direction(Direction.LEFT)
