def first_greater(l, n):
  return next((i for i in l if i > n), None)

print first_greater([2, 10,5,6,80], 6)
print first_greater([2, 10,5,6,80], 20)
print first_greater([2, 10,5,6,80], 100)
