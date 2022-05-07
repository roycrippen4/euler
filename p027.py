# P027

from sympy import sieve, isprime


def main():
    ab = get_possible_ab_values()
    max_consecutive_primes = 0

    for a in range(0, len(ab)):
        for b in range(a, len(ab)):
            c = num_of_consecutive_primes(ab[a], ab[b])
            if c > max_consecutive_primes:
                max_consecutive_primes = c
                x = (ab[a], ab[b], max_consecutive_primes)
                product = ab[a] * ab[b]
    print(x)
    print(product)
    # -59231


def num_of_consecutive_primes(a: int, b: int):
    n = 0
    while isprime(n**2 + a*n + b):
        n += 1
    return n


def get_possible_ab_values():
    ab_values = list(sieve.primerange(1, 1000))
    ab_values.append(1)
    for i in range(0, len(ab_values)):
        ab_values.append(-ab_values[i])
    ab_values.sort()
    return ab_values


if __name__ == "__main__":
    main()
