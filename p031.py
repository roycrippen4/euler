# P031
# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general
# circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many ways can £2 be made using any number of coins?

# 1 1 1 1 1 1 1 1 1 1 = 1       1 1 1 1 1 = 1       1 1 = 1
# 2 1 1 1 1 1 1 1 1   = 2       0 1 1 1 2 = 2       0 2 = 2
# 2 2 1 1 1 1 1 1     = 3       0 0 1 2 2 = 3
# 2 2 2 1 1 1 1       = 4       0 0 0 0 5 = 4
# 2 2 2 2 1 1         = 5       ^simple-ish ^
# 2 2 2 2 2           = 6
# 5 1 1 1 1 1         = 7
# 5 2 1 1 1           = 8
# 5 2 2 1             = 9
# 5 5                 = 10
# 10                  = 11
# how tf do I make this ^ pattern?


import numpy


def main():
    print('confused')


if __name__ == "__main__":
    main()
