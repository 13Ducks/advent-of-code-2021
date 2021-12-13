data = open("day8.txt", "r").read().strip()
data = [l.split(" | ") for l in data.split("\n")]

unique_segment_count = set([2, 4, 3, 7])
count = 0
for line in data:
    output = line[1].split(" ")
    for o in output:
        if len(o) in unique_segment_count:
            count += 1

print("Part 1:", count)

total_output = 0

for line in data:
    signal, output = line
    signal = signal.split(" ")
    output = output.split(" ")

    number_to_code = {}
    for s in signal:
        if len(s) == 2:
            number_to_code[1] = set(s)
        elif len(s) == 3:
            number_to_code[7] = set(s)
        elif len(s) == 4:
            number_to_code[4] = set(s)
        elif len(s) == 7:
            number_to_code[8] = set(s)

    # finding 3 as it is only 5-length with 0 missed intersection with 1
    # finding 2 as it is only 5-length with 2 missed intersection with 4
    for s in signal:
        if len(s) == 5:
            if len(number_to_code[1] - set(s)) == 0:
                number_to_code[3] = set(s)
            if len(number_to_code[4] - set(s)) == 2:
                number_to_code[2] = set(s)

    # finding 5 as it the only 5-length left
    for s in signal:
        if len(s) == 5:
            if set(s) not in number_to_code.values():
                number_to_code[5] = set(s)

    # finding 0 as it is only 6-length with 1 missed intersection with 5
    # finding 9 as it is only 6-length with 0 missed intersection with 3
    for s in signal:
        if len(s) == 6:
            if len(number_to_code[5] - set(s)) == 1:
                number_to_code[0] = set(s)
            if len(number_to_code[3] - set(s)) == 0:
                number_to_code[9] = set(s)

    # finding 6 as it the only 6-length left
    for s in signal:
        if len(s) == 6:
            if set(s) not in number_to_code.values():
                number_to_code[6] = set(s)

    output_value = ""
    for o in output:
        o = set(o)
        for k, v in number_to_code.items():
            if o == v:
                output_value += str(k)

    total_output += int(output_value)

print("Part 2:", total_output)
