# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
from math import factorial as fact



def main():

    def is_divisible(num):
        for i in range(2, 21):
            if num % i != 0:
                return False
        return True


    num = 2520

    while True:
        if is_divisible(num):
            break
        num += 2520
    print(num)


if __name__ == "__main__":
    main()
