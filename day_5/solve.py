def validate_report(report: list[int], rules: dict[int, set[int]]):
    already_seen = set()
    for r in report:
        if r not in rules:
            already_seen.add(r)
            continue

        rule = rules[r]
        invalid_values = rule.intersection(already_seen)
        if len(invalid_values) != 0:
            return False
        already_seen.add(r)

    return True


with open("input") as f:
    rules: dict[int, set[int]] = {}

    for line in f:
        line = line.strip()
        if line == "":
            break

        l1, r1 = line.split("|")
        l1 = int(l1)
        r1 = int(r1)

        if l1 not in rules:
            rules[l1] = set()

        rules[l1].add(r1)

    acc = 0
    for line in f:
        line = line.strip()
        report: list[int] = list(map(int, line.split(",")))
        if validate_report(report, rules):
            acc += report[len(report) // 2]


print(acc)
