# P018
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from
# top to bottom is 23.
#
# `3
# `7  4
#  2 `4  6
#  8  5 `9  3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the given triangle.

def main():
    num_triangle = p018_data_prep()
    num_triangle.reverse()
    for row in range(1, len(num_triangle)):
        for col in range(0, len(num_triangle[row])):
            num_triangle[row][col] += max(num_triangle[row - 1][col], num_triangle[row - 1][col + 1])
    print('ans =', num_triangle[len(num_triangle) - 1][0])  # 1074


def p018_data_prep():
    data = []
    with open('/supplementary_files/p018.txt') as file:
        for line in file:
            data.append([int(i) for i in line.split()])
    return data


if __name__ == "__main__":
    main()
