import numpy as np

data = open("day20.txt", "r").read().strip()
algo, inp = data.split("\n\n")
algo = algo.replace("#", "1").replace(".", "0")
get_algo_v = np.vectorize(lambda x: algo[x])
inp = [list(line) for line in inp.splitlines()]

a = np.array(inp)
a[a == "#"] = 1
a[a == "."] = 0
a = a.astype(int)

for i in range(50):
    # won't work for test input since first char is ".", so empty point stays "."
    # however for real input, first char is "#", so empty points change to "#"
    # and then last char is "." so full points go back to "."
    a = np.pad(a, 2, "constant", constant_values=(i % 2))
    out = np.zeros([a.shape[0] - 2, a.shape[1] - 2], dtype=int)
    out += 2 ** 8 * a[:-2, :-2]
    out += 2 ** 7 * a[:-2, 1:-1]
    out += 2 ** 6 * a[:-2, 2:]
    out += 2 ** 5 * a[1:-1, :-2]
    out += 2 ** 4 * a[1:-1, 1:-1]
    out += 2 ** 3 * a[1:-1, 2:]
    out += 2 ** 2 * a[2:, :-2]
    out += 2 ** 1 * a[2:, 1:-1]
    out += 2 ** 0 * a[2:, 2:]

    out = get_algo_v(out)
    a = out.astype(int)

    if i == 1:
        print("Part 1:", np.unique(a, return_counts=True)[1][1])

print("Part 2:", np.unique(a, return_counts=True)[1][1])