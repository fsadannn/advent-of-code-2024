import re

is_enabled = True


def mul(a, b):
    if not is_enabled:
        return 0
    return a * b


def do():
    global is_enabled
    is_enabled = True
    return 0


def dont():
    global is_enabled
    is_enabled = False
    return 0


with open("input") as f:
    acc = 0
    for line in f:
        for mul_exp in re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line):
            mul_exp = str(mul_exp).replace("'", "")
            r = eval(mul_exp)
            acc += r
    print(acc)
