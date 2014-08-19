def divisble(n, divisors):
    for d in divisors:
        if n%d!=0:
            return False
    return True


#while not divisble(n, [2,3,5,7,11,13,17,19]):
n = 2520
while not divisble(n, range(1,21)):
    n += 2
print n
