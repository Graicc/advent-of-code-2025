import functools

lines = [[int(y) for y in x if y.isdigit()] for x in open("input").readlines()]

## Part 1
total = 0
for line in lines:
    max_value = max(line[:-1])
    max_rest = max(line[line.index(max_value) + 1 :])

    total += max_value * 10 + max_rest

print(total)


## Part 2
@functools.cache
def m(ints: [int], remaining: int) -> int:
    if remaining == 0 or len(ints) == 0:
        return 0

    # Take
    v1 = ints[0]
    v1_max = int(str(v1) + str(m(ints[1:], remaining - 1)))

    # Skip
    v2 = m(ints[1:], remaining)

    return max(v1_max, v2)


# Trailing zero because of the base case
print(sum([m(tuple(line), 12) // 10 for line in lines]))
