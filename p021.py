# P021
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(
# a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
# proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

from utilities import get_proper_divisors


def main():
    cache = {}
    for i in range(1, 1001):
        update_cache(i, cache)
    print(cache)


def update_cache(n, cache):
    divisors = []
    for num in range(1, n):
        if num != 1 and num in cache:
            cache[n] =
        elif n % num == 0 and n != num:
            divisors.append(num)
    cache[n] = divisors
    return cache


if __name__ == "__main__":
    main()
