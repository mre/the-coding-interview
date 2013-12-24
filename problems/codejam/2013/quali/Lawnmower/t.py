lawn = [[2,2,2,2,2],
       [3,1,1,1,3],
       [3,1,1,1,3],
       [2,2,2,2,2]]

lawn = []
sides = lawn[1:-1]
for row in sides:
  print row[0], row[-1]
