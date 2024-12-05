def is_report_safe(report: list[int]):
    is_increasing = report[1] - report[0] >= 0

    for cur, nextt in zip(report, report[1:]):
        diff = nextt - cur
        adiff = abs(diff)

        if is_increasing and diff < 0:
            return False
        elif not is_increasing and diff > 0:
            return False
        elif adiff < 1 or adiff > 3:
            return False

    return True


with open("input", "r") as f:
    acc = 0
    for line in f:
        report = [int(x) for x in line.split()]
        if is_report_safe(report):
            acc += 1
        else:
            for i in range(0, len(report)):
                c_report = report.copy()
                c_report.pop(i)
                if is_report_safe(c_report):
                    acc += 1
                    break

    print(acc)
