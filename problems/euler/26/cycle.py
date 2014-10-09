from decimal import *
from operator import itemgetter

getcontext().prec = 3000

def remainder(quotient):
    remainder = str(quotient)[2:]
    return remainder

def recurring(remainder):
    if len(remainder) == 0:
        return ""
    current_pattern = [remainder[0]]
    for i, r in enumerate(remainder[1:]):
        if r == current_pattern[0]:
            # Check if this is the start of a cycle
            p = remainder[i+1:i+1+len(current_pattern)]
            if "".join(current_pattern) == p:
                return current_pattern
        current_pattern.append(r)
    return ""

def cycle(quotient):
    r = remainder(quotient)
    return "".join(recurring(r))

def quotient(nominator, denominator):
    return Decimal(nominator) / Decimal(denominator)

#lengths = [(d, len(cycle(quotient(1,d)))) for d in range(2,1000)]
#for d,l in lengths:
#    print d,l

print cycle(quotient(1,100))
print cycle(quotient(1,101))
#print max(lengths, key=itemgetter(1))
