# P018


def main():
    num_triangle = p018_data_prep()
    num_triangle.reverse()
    print_triangle(num_triangle)
    for row in range(1, len(num_triangle)):
        for col in range(0, len(num_triangle[row])):
            num_triangle[row][col] += max(num_triangle[row - 1][col], num_triangle[row - 1][col + 1])
        # print_triangle(num_triangle)
    print(num_triangle[len(num_triangle) - 1][0])  # 1074


def print_triangle(xss):
    for xs in xss:
        print(xs)
    print()


def p018_data_prep():
    data = []
    with open('/Users/roycrippen/dev/python/euler/supplementary_files/p018.txt') as file:
        for line in file:
            data.append([int(i) for i in line.split()])
    return data


if __name__ == "__main__":
    main()
