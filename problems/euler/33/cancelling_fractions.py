from itertools import product

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

class Fraction(object):
    def __init__(self, n, d):
        self.n = int(n)
        self.d = int(d)

        if self.d == 0:
            raise ZeroDivisionError

    def __str__(self):
        return '{}/{}'.format(self.n, self.d)

    def to_decimal(self):
        return self.n/(self.d * 1.0)

    def product(self, f):
        return Fraction(self.n * f.nominator(), self.d * f.denominator())

    def nominator(self):
        return self.n

    def denominator(self):
        return self.d

    def simplify(self):
            # Remove greatest common divisor:
            common_divisor = gcd(self.n, self.d)
            return Fraction(self.n / common_divisor, self.d / common_divisor)

def gen_fractions():
    for n in range(10,99):
        for d in range(10,99):
            yield Fraction(n,d)

def filter_digit(number, digit):
    return filter(lambda i: i != digit, str(number))

def is_positive(number):
    return number and int(number) > 0

def gen_cancelled(f):
    for n, d in product(str(f.nominator()), str(f.denominator())):
        if int(n) != 0 and n == d:
            new_nom = filter_digit(f.nominator(), n)
            new_denom = filter_digit(f.denominator(), n)
            if is_positive(new_nom) and is_positive(new_denom):
                yield Fraction(new_nom, new_denom)

def gen_cancelable(f):
    for new_f in gen_cancelled(f):
        if f.to_decimal() == new_f.to_decimal():
            yield (f, new_f)


def main():
    all_cancelable = set()
    for f in gen_fractions():
        if f.to_decimal() < 1:
            all_cancelable.update(gen_cancelable(f))

    result = Fraction(1,1)
    for f, cancelled_f in all_cancelable:
        result = result.product(cancelled_f)

    print result.simplify().denominator()

if __name__ == '__main__':
    main()
