# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# 999 * 999 = 998001 == the largest possible product of two 3-digit numbers.
# we could start at that point, check if it's a palindrome, and if it's not
# subtract one and loop again.

import utilities


def main():
    multipliers = []
    for multiplier in range(90, 101):
        multipliers.append(multiplier)
    print(multipliers)


if __name__ == "__main__":
    main()
