disk: list[str] = []
start_gap_pos: int = 0

with open("input") as f:
    value = f.read(1)
    count = 0
    start_gap_pos = int(value)
    while value != "\n":
        if count % 2 == 1:
            disk.extend(["."] * int(value))
        else:
            disk.extend([count // 2] * int(value))
        count += 1
        value = f.read(1)

# print(disk)

while disk[start_gap_pos] != ".":
    start_gap_pos += 1

last_value_pos = len(disk) - 1
while disk[last_value_pos] == ".":
    last_value_pos -= 1

while last_value_pos > start_gap_pos:
    temp = disk[start_gap_pos]
    disk[start_gap_pos] = disk[last_value_pos]
    disk[last_value_pos] = temp
    while disk[last_value_pos] == ".":
        last_value_pos -= 1
    while disk[start_gap_pos] != ".":
        start_gap_pos += 1

pos = 0
acc = 0
while pos < len(disk) and disk[pos] != ".":
    acc += int(disk[pos]) * pos
    pos += 1


print(acc)
