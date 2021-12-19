import numpy as np

data = open("day16.txt", "r").read().strip()
bits = "".join([f"{int(n,16):04b}" for n in data])

curr_pos = 0
version_sum = 0


def get_int(num_bits):
    global curr_pos
    ret = int(bits[curr_pos : curr_pos + num_bits], 2)
    curr_pos += num_bits
    return ret


def get_literal():
    literal = ""
    not_last_segment = True
    while not_last_segment:
        not_last_segment = bool(get_int(1))
        literal += f"{get_int(4):04b}"
    return int(literal, 2)


operation = [
    sum,
    np.prod,
    min,
    max,
    None,
    lambda s: int(s[0] > s[1]),
    lambda s: int(s[0] < s[1]),
    lambda s: int(s[0] == s[1]),
]


def process_bits():
    global curr_pos, version_sum
    version_sum += get_int(3)

    type_id = get_int(3)
    if type_id == 4:
        return get_literal()
    else:
        length_id = get_int(1)
        subpackets = []

        if not length_id:
            length = get_int(15)
            tmp_pos = curr_pos
            while curr_pos < tmp_pos + length:
                subpackets.append(process_bits())
        else:
            num_subpackets = get_int(11)
            subpackets = [process_bits() for _ in range(num_subpackets)]

        return operation[type_id](subpackets)


output = process_bits()
print("Part 1:", version_sum)
print("Part 2:", output)