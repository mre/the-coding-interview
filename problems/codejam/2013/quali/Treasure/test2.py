from collections import defaultdict
import copy

dataset = defaultdict(list)
dataset[1].append("hello")
d2 = copy.deepcopy(dataset)
d2[1].append("world")
print d2
print dataset
