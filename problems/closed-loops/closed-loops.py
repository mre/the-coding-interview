loops = {"0": 1, "6": 1, "8": 2, "9": 1}


def closed_loops(num):
	t = 0
	for n in list(str(num)):
		if n in loops:
			t += loops[n]
	return t


assert (closed_loops(2816) == 3)
assert (closed_loops(10000) == 4)
assert (closed_loops(16789) == 4)
