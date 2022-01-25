# P003
# The prime factors of 13_195 are 5, 7, 13, and 29
# What is the largest prime factor of the number 600_851_475_143
import math
import utilities.is_prime

def main():
    divisors = []
    n = 13_195
    round_sqrt_n = round(math.sqrt(13_195))

    for num in range(2, round_sqrt_n):
        if n % num == 0:
            divisors.append(num)
    for divisor in divisors:

    print(divisors)


if __name__ == "__main__":
    main()
