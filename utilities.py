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


def find_divisors(n: int):
    divisors = []
    for num in range(2, round(n / 2)):
        if n % num == 0:
            divisors.append(num)
    return divisors
