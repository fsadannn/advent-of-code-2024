def bounded_dfs(expected: int, values: list[int]):
    if len(values) == 2:
        result = values[0] + values[1]

        if result == expected:
            return True

        result = values[0] * values[1]

        if result == expected:
            return True

        result = int(str(values[0]) + str(values[1]))

        return result == expected

    new_value = values[0] + values[1]

    if new_value > expected:
        return False

    if bounded_dfs(expected, [new_value] + values[2:]):
        return True

    new_value = values[0] * values[1]

    if new_value > expected:
        return False

    if bounded_dfs(expected, [new_value] + values[2:]):
        return True

    new_value = int(str(values[0]) + str(values[1]))

    return bounded_dfs(expected, [new_value] + values[2:])


with open("input") as f:
    acc = 0

    for line in f:
        line = line.strip()
        if line == "":
            continue
        _expected, _values = line.split(":", 1)
        expected: int = int(_expected)
        values: list[int] = list(
            map(lambda x: int(x.strip()), filter(lambda z: z != "", _values.split(" ")))
        )

        if bounded_dfs(expected, values):
            acc += expected

print(acc)
