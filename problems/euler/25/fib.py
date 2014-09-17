from itertools import dropwhile, takewhile

def fib():
    a, b = 1, 1
    yield a
    while True:
        a, b = b, a + b
        yield a

for i, f in enumerate(fib()):
    if len(str(f)) == 1000:
           print i + 1 # 0-based
           break
