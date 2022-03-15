# P011 In the given 20x20 grid, what is the greatest product of four adjacent numbers in the same direction (up,
# down, left, right, or diagonally).

from utilities import p011_get_data, p011_get_south, p011_get_east, \
    p011_get_southwest, p011_get_southeast


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
