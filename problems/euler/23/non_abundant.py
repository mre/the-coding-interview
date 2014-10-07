from euler_math import primes_upto, divisors
from itertools import takewhile, combinations_with_replacement

class Abundant(object):

    def __init__(self, limit):
        self.limit = limit
        self.primes = list(primes_upto(limit))
        self.calculate_abundant_numbers()
        self.calculate_pairs()

    def is_abundant(self, n):
        return sum(divisors(n, self.primes)) > n

    def calculate_abundant_numbers(self):
        self.a = [i for i in range(1, self.limit)
                    if self.is_abundant(i)]

    def calculate_pairs(self):
        cwr = combinations_with_replacement
        self.pairs = set(a+b for a,b in cwr(self.a, 2))

    def has_pair(self, n):
        """
        Check nf n can be written as
        the sum of two abundant numbers.
        """
        return n in self.pairs

def main(limit):
    """
    Get sum of all integers which can't be expressed
    as the sum of two abundant numbers
    """
    primes = list(primes_upto(limit))
    abundant = Abundant(limit)
    print sum(i for i in range(1, limit) if not abundant.has_pair(i))

if __name__ == "__main__":
    main(28124)
