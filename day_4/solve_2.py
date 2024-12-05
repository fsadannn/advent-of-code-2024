text_puzzle: list[str] = []

with open("input", "r") as f:
    for line in f:
        line = line.strip()
        if line != "":
            text_puzzle.append(line)

WORD = "MAS"
R_WORD = WORD[::-1]


def check_direction(text: list[str], x: int, y: int):
    if abs(len(text) - y) <= 2 or abs(x - len(text[0])) <= 2:
        return False

    if text[y + 1][x + 1] != "A":
        return False

    d1 = text[y][x] + text[y + 1][x + 1] + text[y + 2][x + 2]
    if d1 != WORD and d1 != R_WORD:
        return False

    d2 = text[y][x + 2] + text[y + 1][x + 1] + text[y + 2][x]
    if d2 != WORD and d2 != R_WORD:
        return False

    return True


acc = 0
for y, line in enumerate(text_puzzle):
    for x in range(len(line)):
        if check_direction(text_puzzle, x, y):
            acc += 1

print(acc)
