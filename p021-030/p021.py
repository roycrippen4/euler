# P021
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n). If d(
# a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
# proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


def main():
    sum_divisors_table = {i: sum_proper_divisors(i) for i in range(2, 10002, 2) if i % 3 != 0}
    total = 0
    for number in sum_divisors_table:
        maybe_idx = sum_divisors_table[number]
        if maybe_idx in sum_divisors_table and number != maybe_idx and sum_divisors_table[maybe_idx] == number:
            total += number
    print(total)  # 31626


def sum_proper_divisors(n: int):
    sum_divisors = 0
    for num in range(1, 1 + int(n / 2)):
        if n % num == 0:
            sum_divisors += num
    return sum_divisors


if __name__ == "__main__":
    main()
