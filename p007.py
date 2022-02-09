# P007
# By listing the first 6 prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10_001st prime number?
from sympy import isprime


def main():
    count = 1
    num = 1
    while count < 10001:
        if isprime(num):
            count += 1
        num += 1
    print(num)
    exit()


if __name__ == "__main__":
    main()
