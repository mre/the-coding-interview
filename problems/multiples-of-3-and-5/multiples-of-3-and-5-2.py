def multiples(n, rrange):
    return [i for i in rrange if i%n == 0]

def sum_multiples(numbers, rrange):
    all_multiples = set()
    for n in numbers:
        all_multiples.update(multiples(n, rrange))
    return sum(all_multiples)

print sum_multiples([3,5], xrange(1,1000))
