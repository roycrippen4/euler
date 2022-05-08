# P030
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4

# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

from utilities import list_digits


def main():
    answer = []
    for i in range(2, 200000):
        if is_power_sum_equal(i, 5):
            answer.append(i)
    print(sum(answer))


def is_power_sum_equal(num: int, power: int):
    p_sum = 0
    digits = list_digits(num)
    for i in range(0, len(digits)):
        p_sum += digits[i] ** power
    return num == p_sum


if __name__ == "__main__":
    main()
