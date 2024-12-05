from collections import defaultdict

ll: list[int] = []
rr: dict[int, int] = defaultdict(lambda: 0)
with open("input") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        l1, r1 = list(filter(lambda x: x != "", line.split(" ")))
        ll.append(int(l1))
        rr[int(r1)] += 1


acc = 0

for l in ll:
    acc += rr[l] * l

print(acc)
