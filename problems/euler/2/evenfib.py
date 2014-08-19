import itertools


MAX_NUM = 4000000

def fib_gen():
    f1, f2 = 1, 2
    yield f1
    yield f2
    while True:
        f1, f2 = f2, f1+f2
        yield f2

even = lambda x: x%2==0
numbers = [fib for fib in itertools.takewhile(lambda fib: fib<MAX_NUM, fib_gen())]
print sum(n for n in numbers if even(n))
