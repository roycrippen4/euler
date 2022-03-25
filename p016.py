# P016
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2 ^ 1000?

def main():
    number_string = str(2 ** 1000)
    summation = 0
    for digit in number_string:
        summation += int(digit)
    print(summation)  # 1366
    print(sum([int(digit) for digit in str(2 ** 1000)]))  # 1366


if __name__ == "__main__":
    main()
