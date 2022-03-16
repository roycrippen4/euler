# P001
# Find the sum of all numbers divisible by 3 and 5 up to 1000

def main():
    i = 1
    total = 0

    while i < 1_000_000:
        if i % 5 is 0 or i % 3 is 0:
            total += i
        i += 1
    print(f'p001 = {total}')


def main1():
    total = 0

    for i in range(1000):
        if i % 5 is 0 or i % 3 is 0:
            total += i
        i += 1
    print(f'p001 = {total}')


if __name__ == "__main__":
    main1()
    main()
