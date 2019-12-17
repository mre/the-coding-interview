# Array Pair Sum

Given an integer array, output all pairs that sum up to a specific value 𝑘.
Consider the fact that the same number can add up to 𝑘 with its duplicates in
the array.

For example the array is `[1, 1, 2, 3, 4]` and the desired sum is `4`. Should we
output the pair `(1, 3)` twice or just once? Also do we output the reverse of a
pair, meaning both `(3, 1)` and `(1, 3)`? Let’s keep the output as short as
possible and print each pair only once. So, we will output only one copy of
`(1, 3)`. Also note that we shouldn’t output `(2, 2)` because it’s not a pair of
two distinct elements.

Your program receives a comma separated list of integers where the first value
is the desired sum 𝑘 and all others are the integers to search for pairs in.
Your output should be a list of comma separated pairs where the lower of the two
numbers is always on the left side:

```
ƒ(10, [3, 4, 5, 6, 7]) -> [(4, 6), (3, 7)]
ƒ( 8, [3, 4, 5, 4, 4]) -> [(3, 5)]
```

## Source

[http://www.ardendertat.com/2011/09/17/programming-interview-questions-1-array-pair-sum/](http://www.ardendertat.com/2011/09/17/programming-interview-questions-1-array-pair-sum/)
