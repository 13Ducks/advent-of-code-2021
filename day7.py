import numpy as np

data = open("day7.txt", "r").read().strip()
pos = np.array([int(n) for n in data.split(",")])

print("Part 1:", int(np.abs(pos - np.median(pos)).sum()))

min_cost = np.inf
for target in range(int(np.median(pos)), int(np.mean(pos) + 1) + 1):
    dist = np.abs(pos - target)
    min_cost = min((dist * (dist + 1) / 2).sum(), min_cost)

print("Part 2:", int(min_cost))