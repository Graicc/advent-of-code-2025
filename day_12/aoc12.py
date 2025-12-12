import numpy as np

lines = open("input").read().split("\n\n")
last = lines[-1].splitlines()
shapes = lines[:-1]
shapes = [
    np.array([[1 if x == "#" else 0 for x in line] for line in shape.splitlines()[1:]])
    for shape in shapes
]

areas = np.array([shape.sum() for shape in shapes])

targets = [
    (
        [int(x) for x in line.split(":")[0].split("x")],
        [int(x) for x in line.split(":")[1].split()],
    )
    for line in last
]

# Didn't expect this heuristic to work :eyeroll:
print(sum([areas @ v <= rows * cols for (rows, cols), v in targets]))
