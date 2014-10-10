from decimal import *
from operator import itemgetter

# Increase the floating point precision.
getcontext().prec = 5000

def remainder(quotient):
    remainder = str(quotient)[2:]
    return remainder

def full_chunks(iterable, chunk_length):
    it_length = len(iterable)
    for start in range(0, it_length, chunk_length):
        if start + chunk_length > it_length:
            # We can't build another full chunk. Stop.
            break
        yield iterable[start:start + chunk_length]

def test_pattern(remainder, length):
    pattern = remainder[:length]
    remaining_chunks = list(full_chunks(remainder, length))
    if len(remaining_chunks) < 2:
        # We can't check because the
        # precision is not sufficient
        # Assume that there won't be a pattern.
        return False
    for chunk in remaining_chunks[1:]:
        if chunk != pattern:
            return False
    return True

def recurring(remainder):
    if len(remainder) == 0:
        return []
    for length in range(1, len(remainder)):
        if test_pattern(remainder, length):
            return remainder[:length]
    return []

def cycle(quotient):
    r = remainder(quotient)
    return "".join(recurring(r))

def quotient(nominator, denominator):
    return Decimal(nominator) / Decimal(denominator)

lengths = [(d, len(cycle(quotient(1,d)))) for d in range(2,1000)]
print max(lengths, key=itemgetter(1))
