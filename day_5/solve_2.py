def validate_report(
    report: list[int], rules: dict[int, set[int]]
) -> (bool, int, set[int]):
    already_seen = set()
    for n, r in enumerate(report):
        if r not in rules:
            already_seen.add(r)
            continue

        rule = rules[r]
        invalid_values = rule.intersection(already_seen)
        if len(invalid_values) != 0:
            return False, n, invalid_values
        already_seen.add(r)

    return True, -1, ()


def fix_report(report: list[int], rules: dict[int, set[int]]) -> (list[int], bool):
    is_valid, invalid_index, invalid_values = validate_report(report, rules)
    if is_valid:
        return report, False

    for i in range(invalid_index, -1, -1):
        if report[i] in invalid_values:
            cp_report = report.copy()
            temp = cp_report[i]
            cp_report[i] = cp_report[invalid_index]
            cp_report[invalid_index] = temp

            t_is_valid, _, _ = validate_report(cp_report, rules)
            if t_is_valid:
                return cp_report, True

            try:
                fixed_report, _ = fix_report(cp_report, rules)
                return fixed_report, True
            except Exception:
                pass

    raise Exception("Could not fix report")


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
        report, is_fixed = fix_report(report, rules)
        if is_fixed:
            acc += report[len(report) // 2]


print(acc)
