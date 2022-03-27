# P020
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!
#
# ans = 648

from math import factorial as fact
from utilities import list_digits_of_n as ld


def main():
    print(sum(ld(fact(100))))  # 648


if __name__ == "__main__":
    main()
