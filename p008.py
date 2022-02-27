# p008
from utilities import get_digit_list


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
    print("this is the answer: ", maximum_product)


if __name__ == "__main__":
    main()
