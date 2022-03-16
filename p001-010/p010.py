# P010
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
from sympy import isprime


def main():
    summation = 2 + 3 + 5
    for i in range(7, 2_000_000, 2):
        # if i % 3 == 0 or i % 5 == 0:
        #     continue
        if isprime(i):
            summation += i
    print(summation)


if __name__ == "__main__":
    main()
