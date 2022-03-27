# P017


number_strings = [
    'One',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Eleven',
    'Twelve',
    'Thirteen',
    'Fourteen',
    'Fifteen',
    'Sixteen',
    'Seventeen',
    'Eighteen',
    'Nineteen',
    'Twenty',
    'Thirty',
    'Forty',
    'Fifty',
    'Sixty',
    'Seventy',
    'Eighty',
    'Ninety',
    'Hundred',
    'Thousand',
    'and'
]


def main():
    answer = 0  # 21124
    for i in range(0, 1000):
        if i < 99:
            answer += process_tens(i)
        elif i < 1000:
            answer += process_hundreds(i)
    print(answer)


def process_tens(i: int):
    curr_number_string = ''
    if i < 20:
        curr_number_string += number_strings[i]
        return len(curr_number_string)  # 1 - 20
    elif (i + 1) % 10 == 0:
        curr_number_string += number_strings[int(i / 10) + 18]
        return len(curr_number_string)  # 30, 40, 50...
    else:
        temp = int(i / 10)
        temp_string = number_strings[temp + 17]
        temp = i % 10
        curr_number_string = temp_string + number_strings[temp]
        return len(curr_number_string)  # 31 - 39, 41 - 49...


def process_hundreds(i: int):
    if i == 999:
        return len(number_strings[0] + number_strings[28])
    if (i + 1) % 100 == 0:  # 100, 200, 300...
        temp = int((i + 1) / 100)
        tens = number_strings[temp - 1]
        curr_number_string = tens + number_strings[27]
        return len(curr_number_string)
    elif i <= 998:
        curr_number_string = number_strings[29]
        hundreds_string = number_strings[int(i / 100) - 1] + number_strings[27]
        return len(hundreds_string + curr_number_string) + process_tens(i % 100)


if __name__ == "__main__":
    main()
