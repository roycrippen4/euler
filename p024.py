# P024

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the
# digits 1, 2, 3 and 4. If all the permutations are listed numerically or alphabetically, we call it lexicographic
# order. The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210 What is the millionth
# lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from utilities import combinations


def main():
    make_combinations(3, 5)


def make_combinations(length: int, value: int):
    limit = combinations(value, length)
    xs = [x for x in range(length)]
    count = 0
    while count < limit:
        print(count)
        count += 1




if __name__ == "__main__":
    main()
