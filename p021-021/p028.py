# P028
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
# 73  74  75  76  77  78  79  80  81
# 72  43  44  45  46  47  48  49  50
# 71  42  21  22  23  24  25  26  51
# 70  41  20  7   8   9   10  27  52
# 69  40  19  6   1   2   11  28  53
# 68  39  18  5   4   3   12  29  54
# 67  38  17  16  15  14  13  30  55
# 66  37  36  35  34  33  32  31  56
# 65  64  63  62  61  60  59  58  57
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def main():
    last_max = 0
    ring_len = 1
    corner_sum = 0

    for i in range(1, 502):
        ring = build_ring(last_max, ring_len)
        last_max = get_prev_max_val(ring)
        ring_len = get_ring_length(i + 1)
        corner_sum += get_corner_sum(ring)
    print(corner_sum)
    # answer = 669171001


def build_ring(last_max: int, ring_len: int):
    return [x for x in range(last_max + 1, last_max + ring_len + 1)]


def get_prev_max_val(ring: list):
    return ring[-1]


def get_ring_length(ring_num: int):
    if ring_num <= 1:
        return 1
    else:
        return (ring_num - 1) * 8


def get_corner_sum(ring: list):
    if len(ring) == 1:
        return 1
    else:
        return sum(ring[::-int(len(ring) / 4)])


if __name__ == "__main__":
    main()
