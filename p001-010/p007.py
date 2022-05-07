# P007
# By listing the first 6 prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10_001st prime number?
from sympy import isprime


def main():
    number_of_primes = 1
    potential_prime = 3
    while number_of_primes < 10001:
        if isprime(potential_prime):
            number_of_primes += 1
        potential_prime += 2
    print(potential_prime - 2)

    # answer is 104_743


if __name__ == "__main__":
    main()
