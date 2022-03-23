# P016
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2 ^ 1000?

def main():
    number = str(2 ** 1000)
    summation = 0
    for digit in number:
        summation = int(digit) + summation
    print(summation)


if __name__ == "__main__":
    main()
