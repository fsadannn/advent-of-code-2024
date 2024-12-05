ll = []
rr = []
with open("input") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        l1, r1 = list(filter(lambda x: x != "", line.split(" ")))
        ll.append(int(l1))
        rr.append(int(r1))

ll.sort()
rr.sort()

acc = 0

for l, r in zip(ll, rr):
    acc += abs(l - r)

print(acc)
