# clean thsi up please

import numpy as np

data = open("day3.txt", "r").read().strip()
arr = []

for line in data.split("\n"):
    arr.append(list(map(int, list(line))))

arr = np.array(arr)
arr = arr.T

one_count = np.count_nonzero(arr == 1, axis=1)
zero_count = np.count_nonzero(arr == 0, axis=1)

gamma = int("".join(map(str, (one_count > zero_count).astype(int).tolist())), 2)
epsilon = int("".join(map(str, (one_count < zero_count).astype(int).tolist())), 2)

print("Part 1:", gamma * epsilon)

arr_copy = np.copy(arr)

for i in range(len(arr)):
    if len(arr[i]) == 1:
        break
    one_count = np.count_nonzero(arr[i] == 1)
    zero_count = np.count_nonzero(arr[i] == 0)
    if one_count >= zero_count:
        arr = arr[:, arr[i] == 1]
    else:
        arr = arr[:, arr[i] == 0]

oxygen = int("".join([str(i) for i in arr.flatten()]), 2)
arr = arr_copy

for i in range(len(arr)):
    if len(arr[i]) == 1:
        break
    one_count = np.count_nonzero(arr[i] == 1)
    zero_count = np.count_nonzero(arr[i] == 0)
    if one_count < zero_count:
        arr = arr[:, arr[i] == 1]
    else:
        arr = arr[:, arr[i] == 0]

co2 = int("".join([str(i) for i in arr.flatten()]), 2)

print("Part 2:", oxygen * co2)
