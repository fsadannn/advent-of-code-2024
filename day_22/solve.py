from math import floor


def next_number(n: int) -> int:
    n = ((n * 64) ^ n) % 16777216
    n = (floor(n / 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n


with open("input") as f:
    acc = 0
    for line in f:
        n = int(line)
        for i in range(2000):
            n = next_number(n)
        acc += n

print(acc)
