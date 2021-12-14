from collections import defaultdict

data = open("day14.txt", "r").read().strip()
compound, rules = data.split("\n\n")
rules = {tuple(r.split(" -> ")[0]): r.split(" -> ")[1] for r in rules.split("\n")}

pairs = defaultdict(int)
for c in zip(compound, compound[1:]):
    pairs[c] += 1

for i in range(40):
    new_pairs = defaultdict(int)
    for pair, v in pairs.items():
        new_pairs[(pair[0], rules[pair])] += v
        new_pairs[(rules[pair], pair[1])] += v
    pairs = new_pairs

    if i == 9 or i == 39:
        elements = defaultdict(int)
        for pair, v in pairs.items():
            elements[pair[0]] += v

        # Need to add last element to count since we are counting first element of pair
        # So last element has no corresponding pair where it is the first element
        elements[compound[-1]] += 1
        element_counts = sorted(elements.values())
        print(
            "Part 1:" if i == 9 else "Part 2:", element_counts[-1] - element_counts[0]
        )
