from collections import namedtuple

Point = namedtuple("Point", ["y", "x"])


def distance(p1: Point, p2: Point):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


class NumericKeyPad:
    def __init__(self):
        self.keypad = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "2"],
            ["", "0", "A"],
        ]
        self._value_pos: dict[str, Point] = {}

        for y, row in enumerate(self.keypad):
            for x, col in enumerate(row):
                self._value_pos[col] = Point(y, x)

        self.current_pos = Point(3, 2)

    def move_to(self, value: str):
        new_pos = self._value_pos[value]

        shortest_path_distante = distance(self.current_pos, new_pos)

        stack
