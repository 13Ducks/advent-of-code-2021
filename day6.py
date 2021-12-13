import numpy as np

data = open("day6.txt", "r").read().strip()
ages = [int(n) for n in data.split(",")]

buckets = np.zeros(9)

initial = np.unique(ages, return_counts=True)
buckets[initial[0]] = initial[1]

for day in range(256):
    buckets = np.roll(buckets, -1)
    buckets[6] += buckets[8]

    if day == 79:
        print("Part 1:", int(buckets.sum()))

print("Part 2:", int(buckets.sum()))
