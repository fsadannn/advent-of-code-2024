Point = tuple[int, int]

antenas: dict[str, list[Point]] = {}
antinodes: set[Point] = set()
W = 0
H = 0

with open("input") as f:
    count = 0

    for y, line in enumerate(f):
        line = line.strip()
        if line == "":
            break
        if W == 0:
            W = len(line)

        for x, c in enumerate(line):
            if c != ".":
                if c not in antenas:
                    antenas[c] = []
                antenas[c].append(Point([y, x]))

        count += 1

    H = count


for nodes in antenas.values():
    if len(nodes) < 2:
        continue

    antinodes.update(nodes)
    for i in range(0, len(nodes) - 1):
        for j in range(i + 1, len(nodes)):
            node1 = nodes[i]
            node2 = nodes[j]
            if node1[1] == 0 and node2[1] == 0:
                distance = abs(node1[0] - node2[0])
                max_node = max(node1[0], node2[0])
                new_pos = max_node + distance
                while new_pos < H:
                    antinodes.add(Point([new_pos, 0]))
                    new_pos += distance
                min_node = min(node1[0], node2[0])
                new_pos = max_node - distance
                while new_pos >= 0:
                    antinodes.add(Point([new_pos, 0]))
                    new_pos -= distance
                continue

            x_distance = abs(node2[1] - node1[1])
            y_distance = abs(node2[0] - node1[0])
            m = (node2[0] - node1[0]) / (node2[1] - node1[1])
            sig = -1 if m < 0 else 1
            node_min = node1
            node_max = node2
            if node_min[1] > node_max[1]:
                t = node_min
                node_min = node_max
                node_max = t

            x = node_max[1] + x_distance
            y = node_max[0] + sig * y_distance
            while x >= 0 and x < W and y >= 0 and y < H:
                antinodes.add(Point([y, x]))
                x += x_distance
                y += sig * y_distance

            x = node_min[1] - x_distance
            y = node_min[0] - sig * y_distance
            while x >= 0 and x < W and y >= 0 and y < H:
                antinodes.add(Point([y, x]))
                x -= x_distance
                y -= sig * y_distance


print(antinodes)
print(len(antinodes))
