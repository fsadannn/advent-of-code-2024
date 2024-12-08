from __future__ import annotations

from joblib import Parallel, delayed

# This is the dummy brute force implementation, try everything
# but parallelized


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


def check_route(
    mapp: list[list[str]], initial_guard_pos: Position, initial_direction: Position
) -> bool:
    direction = initial_direction
    guard_pos = initial_guard_pos
    next_post = guard_pos + direction

    hits = set()

    while (
        next_post.y >= 0
        and next_post.y < len(mapp)
        and next_post.x >= 0
        and next_post.x < len(mapp[0])
    ):
        if mapp[next_post.y][next_post.x] == obstacle:
            p_d = (next_post, direction)
            if p_d in hits:
                return True
            hits.add(p_d)

            direction = direction.rot_90()
            next_post = guard_pos + direction
            continue
        guard_pos = next_post
        next_post = guard_pos + direction

    return False


def check_route_main(
    y: int, mapp: list[list[str]], guard_pos: Position, direction: Position
):

    next_post = guard_pos + direction
    cont = 0

    for x in range(len(mapp[y])):
        if (
            mapp[y][x] == obstacle
            or (guard_pos.y == y and guard_pos.x == x)
            or (next_post.y == y and next_post.x == x)
        ):
            continue

        new_map = mapp[:]
        new_map[y] = mapp[y][:]
        new_map[y][x] = obstacle
        if check_route(new_map, guard_pos, direction):
            cont += 1

    return cont


result = Parallel(n_jobs=-1, verbose=10)(
    delayed(check_route_main)(y, mapp, guard_pos, direction) for y in range(len(mapp))
)

print(sum(result))
