# P026
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
# denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen
# that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


def main():
    max_cycle = 0
    for number in range(2, 1000):
        if number % 5 != 0:
            max_cycle = max(check_cycles(number), max_cycle)
    print(max_cycle + 1, max_cycle)

    # answer = 983


def check_cycles(n: int):
    md = 10 % n
    md_result = set()
    md_result.add(md)

    for cnt in range(2, n + 1):
        md = (10 * md) % n
        if md not in md_result:
            md_result.add(md)
        else:
            return cnt - 1


if __name__ == "__main__":
    main()
