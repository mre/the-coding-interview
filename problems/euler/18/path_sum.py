# Brute force version. Just try all paths.
# This is not optimal, but I can't think of a smarter way to do it right now. :(
# Maybe something like building a binary tree and then going from bottom to top,
# so that we see which paths are possible


class Triangle():
    def __init__(self, triangle):
        self.triangle = triangle

    def paths(self, curr_level=0, curr_pos=0):
        if curr_level >= len(self.triangle):
            yield []
            return
        level = triangle[curr_level]
        left = level[curr_pos]
        for path in self.paths(curr_level+1, curr_pos):
            yield [left] + path
        try:
            right = level[curr_pos+1]
            for path in self.paths(curr_level+1, curr_pos+1):
                yield [right] + path
        except IndexError:
            pass



triangle = [
[75],
[95,64],
[17,47,82],
[18,35,87,10],
[20,4,82,47,65],
[19,1,23,75,3,34],
[88,2,77,73,7,63,67],
[99,65,4,28,6,16,70,92],
[41,41,26,56,83,40,80,70,33],
[41,48,72,33,47,32,37,16,94,29],
[53,71,44,65,25,43,91,52,97,51,14],
[70,11,33,28,77,73,17,78,39,68,17,57],
[91,71,52,38,17,14,91,43,58,5,27,29,48],
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

t = Triangle(triangle)
max = 0
for p in t.paths():
    curr_sum = sum(p)
    if curr_sum > max:
        max = curr_sum
print max
