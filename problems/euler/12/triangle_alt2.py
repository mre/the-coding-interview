def gen_primes(n):
    multiples = set()
    primes = set()
    def primes_upto(n) 
        for p in range(2, n):
            if p not in multiples:
                primes.add(p)
                multiples.update(range(p*2, n, p))
        return primes

def divisors2(n, primes):
    div = set([1, n])
    visited = set()
    if n in primes:
        # A prime number is only
        # divisible by itself and 1
        return div
    for d in range(n/2, 2, -2):
        if n%d == 0:
            div.add(d)
        # Check all multiples
        while d not in primes:
            d /= 2
            if d in visited:
                break
            visited.add(d)
            if d < 2:
                break
            if n%d == 0:
                div.add(d)
    return div

def all_divisors(n, primes):
    # Let's first check the primes 
    matching_primes = [p for p in primes if n%p==0]
    divisors = set(matching_primes)
    visited = set()
    for p in matching_primes:
        for m in range(p*2, n, p):
            if m not in visited:
                if n%m == 0:
                    visited.add(m)
                    divisors.add(m)
                else:
                    # If m does not divide n then all
                    # multiples of m won't either.
                    visited.update(range(m, n, m))
                    break
    return divisors
        

def find_triangle_number(min_divisors):
    estimate = 1
    primes = gen_primes()
    print all_divisors(28, primes)
    exit()
    while divisors(estimate, primes) < min_divisors:
        # Estimate the distance to the
        # triangle number with more than
        # min_divisors
        factor = min_divisors / curr_divisors +1 
        print "Estimate", estimate
        print "Divisors", curr_divisors
        print "Factor", factor
        last = estimate
        estimate *= factor
        curr_divisors = divisors(estimate)
    print estimate
    print last
    for n in xrange(last+1, estimate+1):
        print n
        if divisors(n) >= min_divisors:
            break
    print "Estimate", n
    print "Divisors", divisors(n)

find_triangle_number(500)
