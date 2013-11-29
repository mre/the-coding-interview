from collections import deque
import random

def median_stream():
    median = 0
    stream = deque()
    for i in range(20):
        r = random.randint(1,99999)
        if not stream:
            stream.append(r)
        else:

        if middle[0] < r < middle[1]:
            # Move all right
            middle[2] = middle[1]
            middle[1] = middle[0]
            middle[0] = r
        if middle[1] < r < middle[2]:
            # Move all left
            middle[0] = middle[1]
            middle[1] = middle[2]
            middle[2] = r
        if i % 2 == 0:
            # Median is average of two middle elements
            median = (middle[1] + middle[2]) / 2
        else:
            # Median is middle element
            median = middle[1]
        # Get new value
        print i%2, sorted(middle)
        print median


median_stream()

