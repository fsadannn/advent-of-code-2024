from collections import defaultdict
from math import floor


def next_number(n: int) -> int:
    n = ((n * 64) ^ n) % 16777216
    n = (floor(n / 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n


def last_digit(n: int) -> int:
    return int(str(n)[-1])


class SpecialQueue:
    def __init__(self):
        self.data: list[int] = [0, 0, 0, 0]
        self.index = 0

    def push(self, n: int) -> None:
        self.data[self.index] = n
        self.index = (self.index + 1) % 4

    def get(self):
        return tuple((self.data[(self.index + i) % 4] for i in range(4)))


with open("input") as f:
    changes: dict[tuple[int, int, int, int], int] = defaultdict(lambda: 0)

    for line in f:
        q = SpecialQueue()
        secret_number = int(line.strip())

        for i in range(4):
            next_secret_number = next_number(secret_number)
            q.push(last_digit(next_secret_number) - last_digit(secret_number))
            secret_number = next_secret_number

        local_changes: dict[tuple[int, int, int, int], int] = defaultdict(lambda: 0)

        local_changes[q.get()] += last_digit(secret_number)

        for i in range(2000 - 4):
            next_secret_number = next_number(secret_number)
            next_secret_last_digit = last_digit(next_secret_number)
            q.push(next_secret_last_digit - last_digit(secret_number))
            v = q.get()
            if v not in local_changes:
                local_changes[v] += next_secret_last_digit
            secret_number = next_secret_number

        for v, c in local_changes.items():
            changes[v] += c

m = max(changes.values())
print(m)

# q = SpecialQueue()
# for n, i in enumerate([-3, 6, -1, -1, 0, 2, -2]):
#     q.push(i)
#     if n >= 3:
#         print(n, i, q.get())
