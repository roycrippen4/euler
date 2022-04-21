from math import sqrt, ceil, factorial


def generate_primes(n: int):
    primes = []
    for num in range(0, n + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


# takes a positive integer of any length and returns true if the given number is a palindrome.
def is_palindrome(palindrome):
    palindrome = str(palindrome)
    rev_word = palindrome[::-1]
    return palindrome == rev_word


# takes any string and returns true if the given input is a palindrome, solved recursively
def recursive_is_palindrome(string: str):
    if len(string) == 1:
        return True
    elif len(string) >= 2:
        return string[0] == string[-1]
    else:
        return recursive_is_palindrome(string[1:-1])


# this function takes an integer and returns if the number is prime, the function returns true, otherwise, the function
# returns false.
def is_prime(n: int):
    primes = []
    for num in range(0, n + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    if n in primes:
        return True
    else:
        return False


def get_divisors(n: int):
    divisors = [1]
    for num in range(2, n):
        if n % num == 0:
            divisors.append(num)
    divisors.append(n)
    return divisors


def get_proper_divisors(n: int):
    divisors = []
    for num in range(1, 1 + int(n / 2)):
        if n % num == 0:
            divisors.append(num)
    return divisors


def divisor_sum_list(limit):
    xs = [0] * limit
    for i in range(1, int(limit / 2) + 1):
        j = 2 * i
        while j < limit:
            xs[j] += i
            j += i
    return xs


def how_many_divisors(n: int):
    divisors = 2
    for num in range(2, ceil(sqrt(n))):
        if n % num == 0:
            divisors += 2
    return divisors


def get_digit_list():
    digits = []
    big_number = [
        '73167176531330624919225119674426574742355349194934',
        '96983520312774506326239578318016984801869478851843',
        '85861560789112949495459501737958331952853208805511',
        '12540698747158523863050715693290963295227443043557',
        '66896648950445244523161731856403098711121722383113',
        '62229893423380308135336276614282806444486645238749',
        '30358907296290491560440772390713810515859307960866',
        '70172427121883998797908792274921901699720888093776',
        '65727333001053367881220235421809751254540594752243',
        '52584907711670556013604839586446706324415722155397',
        '53697817977846174064955149290862569321978468622482',
        '83972241375657056057490261407972968652414535100474',
        '82166370484403199890008895243450658541227588666881',
        '16427171479924442928230863465674813919123162824586',
        '17866458359124566529476545682848912883142607690042',
        '24219022671055626321111109370544217506941658960408',
        '07198403850962455444362981230987879927244284909188',
        '84580156166097919133875499200524063689912560717606',
        '05886116467109405077541002256983155200055935729725',
        '71636269561882670428252483600823257530420752963450',
    ]
    # for line in big_number:
    #    digits.extendc
    # return digits


def is_triplet(a: int, b: int):
    return a < b and sqrt(a * a + b * b) % 1 == 0


def combinations(n, r):
    return int(factorial(n) / (factorial(r) * (factorial(n - r))))


def list_digits_of_n(n: int):
    n = str(n)
    digit_list = []
    for i in range(0, len(n)):
        digit_list.append(int(n[i]))
    return digit_list
