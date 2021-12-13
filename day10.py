data = open("day10.txt", "r").read().strip()
lines = data.split("\n")

open_to_close = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}

error_score = 0

only_incomplete = []

for l in lines:
    stack = []
    for c in l:
        errored = False
        if c in open_to_close:
            stack.append(c)
        else:
            if c == open_to_close[stack[-1]]:
                stack.pop()
            else:
                error_score += points[c]
                errored = True
                break

    if not errored:
        only_incomplete.append(l)

print("Part 1:", error_score)

points = {"(": 1, "[": 2, "{": 3, "<": 4}
scores = []

for l in only_incomplete:
    stack = []
    for c in l:
        if c in open_to_close:
            stack.append(c)
        else:
            if c == open_to_close[stack[-1]]:
                stack.pop()

    added = stack[::-1]
    score = 0
    for a in added:
        score *= 5
        score += points[a]

    scores.append(score)

scores.sort()
print("Part 2:", scores[len(scores) // 2])
