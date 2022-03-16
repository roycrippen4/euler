# P012
from utilities import how_many_divisors, get_divisors


def main():
    count = 1
    while True:
        tri = int((count * (count + 1)) / 2)
        count += 1
        if how_many_divisors(tri) >= 500:
            break
    print('\n# =', tri, '\ncount =', count, '\ndivisors =', how_many_divisors(tri))


if __name__ == "__main__":
    main()
