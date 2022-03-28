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
    answer = 0
    for i in range(9999, 218, -1):
        if is_amicable(i):
            answer += i
            print(i)
    print(answer)  # 31626


def sum_proper_divisors(n: int):
    sum_divisors = 0
    for num in range(1, 1 + int(n / 2)):
        if n % num == 0:
            sum_divisors += num
    return sum_divisors


def is_amicable(a):
    b = sum_proper_divisors(a)
    if b != a and a == sum_proper_divisors(b):
        return True


if __name__ == "__main__":
    main()
