from functools import cache

lines = [
    (line.split()[0], line.split()[1:-1], line.split()[-1])
    for line in open("input").readlines()
]
lines = [
    (
        tuple([x == "#" for x in target[1:-1]]),
        tuple([tuple([int(x) for x in button[1:-1].split(",")]) for button in buttons]),
        tuple([int(x) for x in joltage[1:-1].split(",")]),
    )
    for (target, buttons, joltage) in lines
]

# @cache
# def solve(target: tuple[bool], buttons: tuple[set[int]]) -> int:
#     # Click this button


#     # Skip this button

# print(lines)


from itertools import product

total = 0
for target, buttons, _ in lines:
    # print(target, buttons)
    perms = product(*([False, True] for _ in range(len(buttons))))
    ans = 99999
    for perm in perms:
        curr = [False for _ in range(len(target))]

        bs = [b for (take, b) in zip(perm, buttons) if take]
        for b in bs:
            for i in b:
                curr[i] = not curr[i]

        # print(curr, target)
        if tuple(curr) == target:
            ans = min(ans, len(bs))

    if ans == 99999:
        print("ERROR")
    # print(ans)
    total += ans

print(total)
print("")


from functools import lru_cache


# @lru_cache
# def solve(buttons: tuple[tuple[int]], remaining_joltage: tuple[int]) -> int:
#     if sum(remaining_joltage) == 0:
#         return 0

#     # min over all button presses
#     val = 99999
#     for button in buttons:
#         this_joltage = list(remaining_joltage)
#         for b in button:
#             this_joltage[b] -= 1

#         # invalid
#         if any([x < 0 for x in this_joltage]):
#             continue

#         this_val = solve(buttons, tuple(this_joltage))
#         val = min(val, this_val)

#     return val + 1

@lru_cache
def solve(buttons: tuple[tuple[int]], remaining_joltage: tuple[int]) -> int:
    if sum(remaining_joltage) == 0:
        return 0

    



total = 0

for _, buttons, joltage in lines:
    val = solve(buttons, joltage)
    print(val)
    total += val

print(total)
