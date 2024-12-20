disk2: list[tuple[int | str, int]] = []

with open("input") as f:
    value = f.read(1)
    count = 0
    disk_count = 0
    while value != "\n":
        if count % 2 == 1:
            if value != "0":
                disk2.append([".", int(value)])
        else:
            if value != "0":
                disk2.append([count // 2, int(value)])
        count += 1
        value = f.read(1)


last_value_pos = len(disk2) - 1
while disk2[last_value_pos][0] == ".":
    last_value_pos -= 1

current_value = disk2[last_value_pos][0]

while last_value_pos > 0:
    start_gap_pos = -1
    for i in range(0, last_value_pos):
        if disk2[i][0] == "." and disk2[last_value_pos][1] <= disk2[i][1]:
            start_gap_pos = i
            break

    if start_gap_pos == -1:
        last_value_pos -= 1
        while (
            disk2[last_value_pos][0] == "." or disk2[last_value_pos][0] > current_value
        ) and last_value_pos > 0:
            last_value_pos -= 1
        current_value = disk2[last_value_pos][0]
        continue

    temp = disk2[last_value_pos][0]
    if disk2[start_gap_pos][1] > disk2[last_value_pos][1]:
        disk2[start_gap_pos][1] -= disk2[last_value_pos][1]
        disk2[last_value_pos][0] = disk2[start_gap_pos][0]
        disk2.insert(start_gap_pos, [temp, disk2[last_value_pos][1]])
        last_value_pos += 1
    elif disk2[start_gap_pos][1] == disk2[last_value_pos][1]:
        disk2[last_value_pos][0] = disk2[start_gap_pos][0]
        disk2[start_gap_pos][0] = temp

    last_value_pos -= 1

    while (
        disk2[last_value_pos][0] == "." or disk2[last_value_pos][0] > current_value
    ) and last_value_pos > 0:
        last_value_pos -= 1
    current_value = disk2[last_value_pos][0]

pos = 0
acc = 0
for v in disk2:
    if v[0] == ".":
        pos += v[1]
        continue
    val = int(v[0])
    for i in range(v[1]):
        acc += val * pos
        pos += 1


print(acc)
