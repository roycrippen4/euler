# P006
# the difference between the sum of the squares of the first ten natural numbers and the square of the sum
# is 3025 - 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural
# numbers and the square of the sum.


def main():
    square_sum = 0
    sum_square = 0

    for i in range(1, 101):
        square_sum += i
        sum_square += (i ** 2)
    print((square_sum ** 2) - sum_square)


if __name__ == "__main__":
    main()
