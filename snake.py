from position import Position
from direction import Direction


class Snake:
    def __init__(self, board_width, board_height, initial_positions, initial_direction):
        self.board_width = board_width
        self.board_height = board_height
        self.positions = initial_positions
        self.disappear = []
        self.dir = initial_direction
        self.just_ate = False

    def head(self):
        return self.positions[-1]

    def change_direction(self, direction: Direction):
        if Direction.opposite(direction) != self.dir:
            self.dir = direction

    def can_eat(self, position_food):
        self.just_ate = self.head() == position_food
        return self.just_ate

    def move(self):
        self.disappear.clear()
        if not self.just_ate:
            self.disappear.append(self.positions.pop(0))
        match self.dir:
            case Direction.UP:
                delta_pos = Position(0, 1)
            case Direction.RIGHT:
                delta_pos = Position(1, 0)
            case Direction.DOWN:
                delta_pos = Position(0, -1)
            case Direction.LEFT:
                delta_pos = Position(-1, 0)
            case _:
                return Exception("Direction does not exist!")

        head = self.head()
        self.positions.append(head.add(delta_pos))

    def alive(self):
        head = self.head()
        if head.x < 0 or head.x >= self.board_width or head.y < 0 or head.y >= self.board_height:
            return False

        return len(self.positions) == len(set(self.positions))
