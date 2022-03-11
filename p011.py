# P011 In the given 20x20 grid, what is the greatest product of four adjacent numbers in the same direction (up,
# down, left, right, or diagonally).

from utilities import build_p011_grid, p011_check_south, p011_check_east


def main():
    grid = build_p011_grid()
    for y in range(0, len(grid)):
        bucket = grid[y]
        for x in range(0, len(bucket)):
            print(x, y, bucket[x])
            print('can go south?', p011_check_south(y))
            print('can go east?', p011_check_east(x))


if __name__ == "__main__":
    main()
