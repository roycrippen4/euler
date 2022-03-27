# P013
# Work out the first ten digits of the sum of the given one-hundred 50-digit numbers.


def main():
    big_num = str(p013_get_sum())
    answer = ''
    for i in range(0, 10):
        answer += str(big_num[i])
    print(answer)  # 5537376230


def p013_get_sum():
    with open('/supplementary_files/p013_digits.txt') as file:
        big_num = 0
        for line in file:
            split_line = [int(i) for i in line.split()]
            big_num += split_line[0]
    return big_num


if __name__ == "__main__":
    main()
