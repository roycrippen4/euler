# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# 999 * 999 = 998001 == the largest possible product of two 3-digit numbers.
# given range (10, 13)
# Desired behavior:
# 10  10  100
# 10  11  110
# 10  12  120
# 10  13  130
# 11  11  121
# 11  12  132
# 11  13  143
# 12  12  144
# 12  13  156
# 13  13  169
from utilities import is_palindrome


def main():
    lower = 100
    upper = 1000
    palindromes = []
    while upper >= lower:
        for number in range(lower, upper):
            if is_palindrome(lower * number) and (lower * number) not in palindromes:
                palindromes.append(lower * number)
        lower += 1
    palindromes.sort()
    print(palindromes.pop())


def p004():
    big_palindrome = 0
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            candidate = i * j
            if is_palindrome(candidate) and candidate > big_palindrome:
                big_palindrome = candidate
            if candidate < big_palindrome:
                break
    print(big_palindrome)


if __name__ == "__main__":
    p004()
