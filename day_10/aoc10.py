from itertools import product
import numpy as np
from scipy.optimize import linprog

lines = [
    (line.split()[0], line.split()[1:-1], line.split()[-1])
    for line in open("input").readlines()
]
lines = [
    (
        [x == "#" for x in target[1:-1]],
        [[int(x) for x in button[1:-1].split(",")] for button in buttons],
        [int(x) for x in joltage[1:-1].split(",")],
    )
    for (target, buttons, joltage) in lines
]

## Part 1
total = 0
for target, buttons, _ in lines:
    perms = product(*[[False, True] for _ in range(len(buttons))])

    ans = 99999
    for perm in perms:
        curr = [False for _ in range(len(target))]

        bs = [b for (take, b) in zip(perm, buttons) if take]
        for b in bs:
            for i in b:
                curr[i] = not curr[i]

        if curr == target:
            ans = min(ans, len(bs))

    if ans == 99999:
        print("ERROR")

    total += ans

print(total)


## Part 2
def solve(buttons: list[list[int]], joltage: list[int]) -> int:
    # print(buttons)
    # print(joltage)
    # minimize button presses using linear programming
    num_buttons = len(buttons)
    num_joltage = len(joltage)
    c = np.ones(num_buttons)

    A_eq = np.zeros((num_joltage, num_buttons))
    for i, button in enumerate(buttons):
        A_eq[:, i] = [1 if x in button else 0 for x in range(num_joltage)]

    b_eq = joltage

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), integrality=1)
    return int(res.fun)


print(sum([solve(buttons, joltage) for (_, buttons, joltage) in lines]))
