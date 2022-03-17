# P014
from utilities import get_len_collatz


def main():
    cache = {}
    for i in range(2, 10):
        print(get_len_collatz(i, cache))


if __name__ == "__main__":
    main()
