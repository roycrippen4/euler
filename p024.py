# P024

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the
# digits 1, 2, 3 and 4. If all the permutations are listed numerically or alphabetically, we call it lexicographic
# order. The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210 What is the millionth
# lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import math


def main():
    perm([0, 1, 2])


def perm(xs):
    # prints out the input, is the first permutation
    print(1, xs)

    # need the length of xs, is used multiple times
    length = len(xs)
    n = length - 1

    # the number of permutations for a given set of numbers is count = fact(len(xs))
    perm_count = math.factorial(length)

    for c in range(1, perm_count):
        # if xs = [0, 1, 2]
        # i = (len(xs) - 1) - 1 = 1
        # j = (len(xs) - 1) = 2
        i = n - 1
        j = n

        while xs[i] > xs[i + 1]:
            i -= 1
        while xs[j] < xs[i]:
            j -= 1
        xs[i], xs[j] = xs[j], xs[i]
        j = n
        i += 1
        while i < j:
            xs[i], xs[j] = xs[j], xs[i]
            i += 1
            j -= 1
        print(c + 1, xs)


if __name__ == "__main__":
    main()
