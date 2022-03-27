# P014

def main():
    cache = {}
    for i in range(2, 1_000_000):
        get_len_collatz(i, cache)
    print(max(zip(cache.values(), cache.keys()))[1])  # ans = 837799


def get_len_collatz(i: int, cache):
    count = 1
    n = i
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        if n in cache:
            cache[i] = cache[n] + count
            return
        count += 1
    cache[i] = count
    return


if __name__ == "__main__":
    main()
