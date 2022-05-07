# P015
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20×20 grid?
from utilities import combinations


def main():
    # 20x20 grid
    # (x + y)! / x! * y! == n! / (r! * (n - r)!)
    print(combinations(40, 20))


if __name__ == "__main__":
    main()
