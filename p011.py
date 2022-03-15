# P011 In the given 20x20 grid, what is the greatest product of four adjacent numbers in the same direction (up,
# down, left, right, or diagonally).

def p011_get_data():
    grid = []
    with open('/Users/roycrippen/dev/python/euler/supplementary_files/p011_grid') as file:
        for line in file:
            split_line = [int(i) for i in line.split()]
            grid.append(split_line)
    return grid


def p011_get_south(x, y, grid):
    current_product = 0
    if y < 17:
        current_product = grid[y][x] * grid[y + 1][x] * grid[y + 2][x] * grid[y + 3][x]
    return current_product


def p011_get_east(x, y, grid):
    current_product = 0
    if x < 17:
        current_product = grid[y][x] * grid[y][x + 1] * grid[y][x + 2] * grid[y][x + 3]
    return current_product


def p011_get_southeast(x, y, grid):
    current_product = 0
    if x < 17 and y < 17:
        current_product = grid[y][x] * grid[y + 1][x + 1] * grid[y + 2][x + 2] * grid[y + 3][x + 3]
    return current_product


def p011_get_southwest(x, y, grid):
    current_product = 0
    if x > 2 and y < 17:
        current_product = grid[y][x] * grid[y + 1][x - 1] * grid[y + 2][x - 2] * grid[y + 3][x - 3]
    return current_product


def main():
    grid = p011_get_data()
    products = []
    for x in range(0, len(grid)):
        for y in range(0, len(grid)):
            products.append(p011_get_south(x, y, grid))
            products.append(p011_get_east(x, y, grid))
            products.append(p011_get_southwest(x, y, grid))
            products.append(p011_get_southeast(x, y, grid))
    print(max(products))


if __name__ == "__main__":
    main()
