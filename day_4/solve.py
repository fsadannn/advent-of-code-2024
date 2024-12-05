text_puzzle: list[str] = []

with open("input", "r") as f:
    for line in f:
        line = line.strip()
        if line != "":
            text_puzzle.append(line)

DOWN = 0
LEFT = 1
DIAG_L = 3
DIAG_R = 4

WORD = "XMAS"
R_WORD = WORD[::-1]


def check_direction(
    text: list[str], x: int, y: int, direction: DOWN | DIAG_L | LEFT | DIAG_R  # type: ignore
):
    if y == 7:
        pass
    if abs(len(text) - y) <= 3 and direction in [DOWN, DIAG_R, DIAG_L]:
        return False

    if x < 3 and direction in [LEFT, DIAG_L]:
        return False

    if abs(x - len(text[0])) <= 3 and direction in [DIAG_R]:
        return False

    # let = []

    word = ""
    if text[y][x] == WORD[0]:
        word = WORD
    elif text[y][x] == R_WORD[0]:
        word = R_WORD
    else:
        return False

    for i, letter in enumerate(word):
        xx = x
        yy = y
        if direction in [DOWN, DIAG_R, DIAG_L]:
            yy += i
        if direction in [LEFT, DIAG_L]:
            xx -= i
        if direction in [DIAG_R]:
            xx += i
        if text[yy][xx] != letter:
            return False
        # let.append((yy, xx, text[yy][xx]))

    # print(let)
    return True


acc = 0
for y, line in enumerate(text_puzzle):
    for x in range(len(line)):
        if check_direction(text_puzzle, x, y, DOWN):
            acc += 1
        if check_direction(text_puzzle, x, y, LEFT):
            acc += 1
        if check_direction(text_puzzle, x, y, DIAG_L):
            acc += 1
        if check_direction(text_puzzle, x, y, DIAG_R):
            acc += 1

print(acc)
