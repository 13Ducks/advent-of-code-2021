import re

data = open("day17.txt", "r").read().strip()
x1, x2, y1, y2 = list(map(int, re.findall(r"[-\d]+", data)))
print("Part 1:", int((y1 * (y1 + 1)) / 2))

possible_cnt = 0
for x in range(1, x2 + 1):
    for y in range(y1, -y1 + 1):
        curr_x, curr_y = 0, 0
        dx, dy = x, y
        while curr_y >= y1:
            curr_x += dx
            curr_y += dy
            dx -= (dx > 0) - (dx < 0)
            dy -= 1

            if x1 <= curr_x <= x2 and y1 <= curr_y <= y2:
                possible_cnt += 1
                break

print("Part 2:", possible_cnt)