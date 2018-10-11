n = 100
sum_of_squares = sum(x**2 for x in range(1,n+1))
print sum_of_squares
square_of_sum = sum(x for x in range(1,n+1))**2
print square_of_sum
diff = sum_of_squares - square_of_sum
print diff
