lines = [x.split() for x in open("input").readlines()]

last = lines.pop()

## Part 1
total = 0

for i, op in enumerate(last):
    this_line = [int(line[i]) for line in lines]
    if op == "*":
        curr = 1
        for x in this_line:
            curr *= x
        total += curr
    else:
        curr = 0
        for x in this_line:
            curr += x
        total += curr

print(total)


## Part 2
import numpy as np

lines = [list(line) for line in open("input").readlines()[:-1]]
lines = np.array(lines)
lines = lines.transpose()

i = 0

total = 0
curr = -1
for line in lines:
    s = "".join(line).strip()
    if len(s) == 0:
        i += 1
        total += curr
        curr = -1
        continue

    val = int(s)

    if curr == -1:
        curr = val
        continue

    if last[i] == "*":
        curr *= val
    else:
        curr += val

print(total)
