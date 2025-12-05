ranges, ids = open("input").read().split("\n\n")

ranges = [tuple([int(x) for x in line.split("-")]) for line in ranges.splitlines()]
ids = [int(x) for x in ids.splitlines()]

# Part 1
total = 0
for id in ids:
    for lower, upper in ranges:
        if id >= lower and id <= upper:
            total += 1
            break

print(total)

# Part 2
rs = []


def merge(r1: tuple[int, int], r2: tuple[int, int]) -> tuple[int, int] | None:
    (l1, u1) = r1
    (l2, u2) = r2

    if (
        (u1 >= l2 and l1 <= l2)
        or (u1 >= u2 and l1 <= u2)
        or (l1 >= l2 and u1 <= u2)
        or (l2 >= l1 and u2 <= u1)
    ):
        return (min(l1, l2), max(u1, u2))

    return None


# Merge each range in
while len(ranges) > 0:
    r1 = ranges.pop()
    found = False
    for i in range(len(rs)):
        m = merge(r1, rs[i])
        if m is not None:
            rs[i] = m
            found = True
            break
    if not found:
        rs.append(r1)


# Merge resulting
def inner():
    for r1 in range(len(rs)):
        for r2 in range(r1 + 1, len(rs)):
            m = merge(rs[r1], rs[r2])
            if m is not None:
                rs[r1] = m
                rs.pop(r2)
                return True

    return False


found = True
while found:
    found = inner()


# Sum up disjoint ranges
print(sum([u - l + 1 for (l, u) in rs]))
