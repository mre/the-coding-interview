def intersections(lst1,lst2):
    return [i for i in lst1 if i in lst2]


print(intersections(['dog', 'cat', 'egg'], ['cat', 'dog', 'chicken']))