# P006
# the difference between the sum of the squares of the first ten natural numbers and the square of the sum
# is 3025 - 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural
# numbers and the square of the sum.


def main():
    squaresum = 0
    sumsquare = 0

    for i in range(1, 101):
        squaresum += i
        sumsquare += (i ** 2)
    print((squaresum ** 2) - sumsquare)


if __name__ == "__main__":
    main()
