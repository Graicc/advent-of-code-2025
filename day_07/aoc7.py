import functools

lines = open("input").readlines()

## Part 1
positions = set([lines[0].find("S")])

total = 0
for line in lines[1:]:
    next_positions = set()
    for position in positions:
        if line[position] == ".":
            next_positions.add(position)
        elif line[position] == "^":
            next_positions.add(position - 1)
            next_positions.add(position + 1)
            total += 1

    positions = next_positions

print(total)


## Part 2
@functools.cache
def m(position: int, idx: int) -> int:
    if idx >= len(lines):
        return 1

    if lines[idx][position] == "^":
        return m(position - 1, idx + 2) + m(position + 1, idx + 2)
    else:
        return m(position, idx + 2)


print(m(lines[0].find("S"), 2))
