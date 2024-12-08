from __future__ import annotations


class Position:
    def __init__(self, y: int, x: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __o: Position) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __hash__(self) -> int:
        return hash((self.y, self.x))

    def __repr__(self) -> str:
        return f"({self.y}, {self.x})"

    def __add__(self, __o: Position) -> Position:
        return Position(self.y + __o.y, self.x + __o.x)

    def __sub__(self, __o: Position) -> Position:
        return Position(self.y - __o.y, self.x - __o.x)

    def rot_90(self) -> Position:
        if self.x == 0:
            if self.y == -1:
                return Position(0, 1)
            else:
                return Position(0, -1)

        return Position(self.x, 0)


visited = set()

mapp: list[list[str]] = []
guard_pos = Position(0, 0)
guard_values = ("^", ">", "v", "<")
direction = Position(0, 0)
obstacle = "#"


def get_direction(guard_value: str) -> Position:
    if guard_value == "^":
        return Position(-1, 0)
    elif guard_value == ">":
        return Position(0, 1)
    elif guard_value == "v":
        return Position(1, 0)
    elif guard_value == "<":
        return Position(0, -1)


with open("input") as f:
    for line in f:
        line = line.strip()
        if line == "":
            break
        mapp.append([])
        for cell in line:
            mapp[-1].append(cell)
            if cell in guard_values:
                guard_pos = Position(len(mapp) - 1, len(mapp[-1]) - 1)
                direction = get_direction(cell)
                visited.add(guard_pos)

next_post = guard_pos + direction

while (
    next_post.y >= 0
    and next_post.y < len(mapp)
    and next_post.x >= 0
    and next_post.x < len(mapp[0])
):
    if mapp[next_post.y][next_post.x] == obstacle:
        direction = direction.rot_90()
        next_post = guard_pos + direction
        continue
    guard_pos = next_post
    visited.add(guard_pos)
    next_post = guard_pos + direction


print(len(visited))
