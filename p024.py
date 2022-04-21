# P024

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the
# digits 1, 2, 3 and 4. If all the permutations are listed numerically or alphabetically, we call it lexicographic
# order. The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210 What is the millionth
# lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from utilities import recursive_is_palindrome


def main():
    xs = [0, 1, 2]
    print(all_combos(xs))


def all_combos(xs: list):
    if len(xs) == 0:
        return [[]]

    first_element = xs[0]
    xs.remove(xs[0])

    combs_without_first = all_combos(xs)
    combs_with_first = []

    for i in combs_without_first:
        combs_with_first.append(combs_without_first[i])





if __name__ == "__main__":
    main()
