# p008
#
from utilities import get_digit_list
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832. Find the
# thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?


def main():
    digit_list = get_digit_list()
    current_product = 1
    maximum_product = 0
    width = 13

    for i in range(0, 997):
        if i + width > 997:
            break
        for j in range(i, i + width):
            current_product *= digit_list[j]
        if maximum_product < current_product:
            maximum_product = current_product
        current_product = 1
    print("The greatest product that can be constructed from 13 adjacent digits within the given number is:"
          "", maximum_product)


if __name__ == "__main__":
    main()
