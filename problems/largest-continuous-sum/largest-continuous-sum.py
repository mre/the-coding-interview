def largest_continous(l):
    """
    Runtime: O(n)
    """
    max_sum = 0
    start = 0
    end = 1
    while (end <= len(l)):
        if l[start] + l[start+1] > 0:
            curr_sum = sum(l[start:end])
            max_sum = max(curr_sum, max_sum)
            end += 1
        else:
            # Start new sequence
            start = end + 1
            end = start + 1
    return max_sum

print largest_continous([5,-2,6,-3,12,24,-1,1,3])
