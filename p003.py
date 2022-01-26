# P003
# The prime factors of 13_195 are 5, 7, 13, and 29
# What is the largest prime factor of the number 600_851_475_143
import math
from sympy import isprime


def main():
    prime_divisors = []
    divisors = []
    n = 600_851_475_143
    round_sqrt_n = round(math.sqrt(n))

    for num in range(2, round_sqrt_n):
        if n % num == 0:
            divisors.append(num)
    for divisor in divisors:
        if isprime(divisor):
            prime_divisors.append(divisor)

    print(prime_divisors.pop())


if __name__ == "__main__":
    main()
