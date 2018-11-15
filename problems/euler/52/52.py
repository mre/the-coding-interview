"""
Euler Problem: 52

It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 
2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""

def permutedMutables(num):
	dig_set = set(str(num))
  for i in range(2, 7):
		val = num * i
		val_set = set(str(val))
		if not dig_set == val_set:
			return False
	return True

def euler52():
	num = 2
	result = False
	while not result:
		result = permutedMutables(num)
		if not result:
			num += 1
	return num

print(euler52())
