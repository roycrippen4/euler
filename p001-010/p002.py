# P002
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms.

def main():
    prev_digit = 0
    curr_digit = 1
    even_fibs_sum = 0

    while curr_digit < 4_000_000:
        next_digit = prev_digit + curr_digit
        prev_digit = curr_digit
        curr_digit = next_digit
        if prev_digit % 2 is 0:
            even_fibs_sum += prev_digit
    print(even_fibs_sum)


if __name__ == "__main__":
    main()
