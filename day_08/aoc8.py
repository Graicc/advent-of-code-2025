lines = [tuple([int(x) for x in line.split(",")]) for line in open("input").readlines()]


def dist(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    x, y, z = a
    a, b, c = b

    return (x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2


# Get all pairs of elements (order insensitive)
perms = []
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        perms.append((lines[i], lines[j]))

perms.sort(key=lambda a: dist(*a), reverse=True)

sets: list[set[tuple[int, int, int]]] = []

iteration_count = 0

while True:
    iteration_count += 1

    a, b = perms.pop()

    # Find sets with a and b
    i_a = None
    i_b = None
    for s in range(len(sets)):
        if a in sets[s]:
            i_a = s
        if b in sets[s]:
            i_b = s

    if i_a is not None and i_b is not None:
        # Already in same circuit, do nothing
        if i_a == i_b:
            continue

        # Combine separate circuits
        sets[i_a] = sets[i_a].union(sets[i_b])
        sets.pop(i_b)
    elif i_a is not None:
        # Add b to a's
        sets[i_a].add(b)
    elif i_b is not None:
        # Add a to b's
        sets[i_b].add(a)
    else:
        # New circuit
        sets.append(set([a, b]))

    # Part 1
    lens = [len(s) for s in sets]
    if iteration_count == 1000:
        lens.sort(reverse=True)
        print(lens[0] * lens[1] * lens[2])

    # Part 2
    if sum(lens) == len(lines):
        print(a[0] * b[0])
        break
