import numpy as np
from scipy import signal

grid = np.array(
    [[1 if c == "@" else 0 for c in line] for line in open("input").readlines()]
)

kernal = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])

# Part 1
conv = signal.convolve(grid, kernal, mode="same")

print(np.logical_and(conv < 4, grid == 1).sum())

# Part 2
total = 0
while True:
    conv = signal.convolve(grid, kernal, mode="same")

    to_remove = np.logical_and(conv < 4, grid == 1)
    to_remove_sum = to_remove.sum()
    if to_remove_sum == 0:
        break

    total += to_remove_sum
    grid[to_remove] = 0

print(total)
