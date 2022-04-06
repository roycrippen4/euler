# P023

# create a list of the sum of divisors of the first 10000 numbers.

# check each number, i, in the divisor_sum_list to see if that number is abundant. If the number is abundant,
# append that number to a new list. If the number is not abundant, we will append False into the same list.

# okay, so now we have a list of abundant numbers, with the greatest abundant number being 1 less than the max
# of the analytical limit of numbers that can be comprised as a sum of two abundant numbers. so that's cool.

# now we need to construct a shitload of sums of abundant numbers. try to add every element of the list to every
# other element of the list.


def main():
    n = 35
    divisor_list = divisor_sum_list(n)
    abundant_list = abundant_num_list(divisor_list)
    answer = 0
    inner_list = list(zip([j for j in range(0, len(abundant_list))], abundant_list))

    for i in range(0, n):
        for (j, ab) in inner_list:
            if ab:
                print(j, 'is abundant')
                if j >= i:
                    print(j, '>=', i)
                    answer += i
                    print('answer is', answer)
                    break
                if abundant_list[i - j]:
                    break
    print(answer)


def is_abundant(n: int, divisor_list: list):
    return n < divisor_list[n]


def divisor_sum_list(limit):
    xs = [0] * limit
    for i in range(1, int(limit / 2) + 1):
        j = 2 * i
        while j < limit:
            xs[j] += i
            j += i
    return xs


def abundant_num_list(xs: list):
    abundant_numbers = []
    for x in range(0, len(xs)):
        abundant_numbers.append(is_abundant(x, xs))
    return abundant_numbers


if __name__ == "__main__":
    main()
