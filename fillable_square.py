import pyglet

BACKGROUND = (0, 0, 0)
EMPTY = (255, 255, 255)

class FillableSquare:
    def __init__(self, x, y, side, filled=False, batch=None, offset_x=0, offset_y=0):
        self.x = x
        self.y = y
        self.side = side
        self.filled = filled
        self.batch = batch
        self.offset_x = offset_x
        self.offset_y = offset_y

        self.border_size = side / 7

        self.outside = pyglet.shapes.Rectangle(x=self.x * self.side + self.offset_x,
                                               y=self.y * self.side + self.offset_y,
                                               width=self.side, height=self.side,
                                               color=BACKGROUND,
                                               batch=self.batch)

        self.inside = pyglet.shapes.Rectangle(x=self.x * self.side + self.offset_x + (self.border_size // 2),
                                              y=self.y * self.side + self.offset_y + (self.border_size // 2),
                                              width=self.side - self.border_size, height=self.side - self.border_size,
                                              color=EMPTY, batch=self.batch)

    def flip_filled(self):
        if self.filled:
            self.empty()
        else:
            self.fill()

    def fill(self):
        self.inside.color = BACKGROUND
        self.filled = True

    def empty(self):
        self.inside.color = EMPTY
        self.filled = False
