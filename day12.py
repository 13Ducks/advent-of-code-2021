from collections import defaultdict

data = open("day12.txt", "r").read().strip()
paths = data.split("\n")

graph = defaultdict(list)
for p in paths:
    start, end = p.split("-")
    graph[start].append(end)
    graph[end].append(start)


def find_paths(start, end, seen, curr_path, finished, visited_small_twice, part2):
    if start.islower():
        seen.add(start)
    curr_path.append(start)

    if start == end:
        finished.add(" ".join(curr_path))
    else:
        for n in graph[start]:
            if n not in seen:
                if (
                    part2
                    and start.islower()
                    and not visited_small_twice
                    and start not in ["start", "end"]
                ):
                    seen.remove(start)
                    find_paths(n, end, seen, curr_path, finished, True, part2)
                    seen.add(start)

                find_paths(
                    n, end, seen, curr_path, finished, visited_small_twice, part2
                )

    if start in seen:
        seen.remove(start)
    curr_path.pop()


seen = set()
finished = set()
find_paths("start", "end", seen, [], finished, False, part2=False)
print("Part 1:", len(finished))

seen = set()
finished = set()
find_paths("start", "end", seen, [], finished, False, part2=True)
print("Part 2:", len(finished))
