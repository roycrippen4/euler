# P009
# A Pythagorean triplet is a set of three natural numbers (positive integers, sometimes zero), a < b < c, for which,
# a^2 + b^2 = c^2.
# Example: 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
from utilities import is_triplet, generate_primes
from math import sqrt


def main():
    for i in range(1, 500):
        for j in range(i + 1, 500):
            if is_triplet(i, j):
                k = int(sqrt(i * i + j * j))
                if i < j < k and i + j + k == 1000:
                    print(i * j * k)
                    exit()


if __name__ == "__main__":
    main()
