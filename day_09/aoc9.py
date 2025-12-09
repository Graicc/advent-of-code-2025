from bisect import bisect, bisect_left
from collections import defaultdict
from itertools import chain

lines = [tuple([int(x) for x in line.split(",")]) for line in open("input").readlines()]

perms = []
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        perms.append((lines[i], lines[j]))

## Part 1
print(
    max([((abs(ax - bx) + 1) * (abs(ay - by) + 1)) for ((ax, ay), (bx, by)) in perms])
)

## Part 2

# Adjacent points with wrap around
adj = chain(zip(lines, lines[1:]), [(lines[-1], lines[0])])

# hlines is a lookup from y pos -> list of (left, right)
hlinesl = [(ay, (min(ax, bx), max(ax, bx))) for ((ax, ay), (bx, by)) in adj if ay == by]
hlines = defaultdict(list)
for y, h in hlinesl:
    hlines[y].append(h)

# yunique is the sorted y values that appear in the input
yunique = sorted(hlines.keys())

# vlines is a lookup from x pos -> list of (bottom, top)
adj = chain(zip(lines, lines[1:]), [(lines[-1], lines[0])])
vlinesl = [(ax, (min(ay, by), max(ay, by))) for ((ax, ay), (bx, by)) in adj if ax == bx]
vlines = defaultdict(list)
for x, v in vlinesl:
    vlines[x].append(v)

# xunique is the sorted x values that appear in the input
xunique = sorted(vlines.keys())


# By presorting perms we know that the first one we find will be the largest
perms.sort(
    key=lambda a: (abs(a[0][0] - a[1][0]) + 1) * (abs(a[0][1] - a[1][1]) + 1),
    reverse=True,
)


# Check if x,y is inside the shape
# Uses a raycast: fire a ray towards y=0. If it hits an odd number of lines, we are on the inside
# By using the yunique list, we can skip to only the meaningful parts of the raycast
def inside(x: int, y: int) -> bool:
    xi = bisect(xunique, x)
    yi = bisect(yunique, y)

    # Handle edge cases where we are on an edge
    if any([x >= ax and x <= bx for (ax, bx) in hlines[y]]):
        return True

    if any([y >= ay and y <= by for (ay, by) in vlines[x]]):
        return True

    res = False

    while yi > 0:
        yi -= 1
        pairs = hlines[yunique[yi]]

        if any([x >= ax and x < bx for (ax, bx) in pairs]):
            res = not res

    return res


# Check if a rectangle is inside the shape
# It does this by checking the perimeter of the shape
# For speed, you can skip most of the perimeter, and instead only check values next to a unique value
# (next to a value where there is an edge somewhere on that line)
def check(ax: int, ay: int, bx: int, by: int):
    (ax, bx) = sorted((ax, bx))
    (ay, by) = sorted((ay, by))

    # The ranges to check in unique space
    x_start = bisect_left(xunique, ax)
    x_end = bisect(xunique, bx)
    y_start = bisect_left(yunique, ay)
    y_end = bisect(yunique, by)

    # The values to check on either side of the unique values (in world space)
    xs = list(
        chain.from_iterable(
            [[xunique[x] - 1, xunique[x] + 1] for x in range(x_start, x_end)]
        )
    )[1:-1]
    ys = list(
        chain.from_iterable(
            [[yunique[y] - 1, yunique[y] + 1] for y in range(y_start, y_end)]
        )
    )[1:-1]

    # Check all the relevant values
    for x in xs:
        if not inside(x, ay) or not inside(x, by):
            return False

    for y in ys:
        if not inside(ax, y) or not inside(bx, y):
            return False

    return True


# iter = 0
for (ax, ay), (bx, by) in perms:
    # iter += 1
    # if iter % 100 == 0:
    #     print("iter ", iter, " out of ", len(perms))

    if check(ax, ay, bx, by):
        print((abs(ax - bx) + 1) * (abs(ay - by) + 1))
        break

# # Debug visualization
# for i in range(10):
#     line = ""
#     for j in range(20):
#         line += "O" if (j, i) in lines else "X" if inside(j, i) else " "
#     print(line)
