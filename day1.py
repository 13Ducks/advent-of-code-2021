data = open("day1.txt", "r").read().strip()
data = list(map(int, data.split("\n")))

p1 = 0

for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        p1 += 1

print("Part 1:", p1)

curr = sum(data[:2])
p2 = 0

for i in range(3, len(data)):
    new = curr + data[i] - data[i - 3]
    if new > curr:
        p2 += 1

    curr = new

print("Part 2:", p2)
