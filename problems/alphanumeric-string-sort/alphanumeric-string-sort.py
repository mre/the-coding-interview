def alphanum_sort(alphanum_string):
    char_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0246813579"
    return ''.join(sorted(alphanum_string, key=char_string.index))

print(alphanum_sort("Sorting0123456789"))             # ginortS0246813579
print(alphanum_sort("foobar1237348421"))              # abfoor2244811337
print(alphanum_sort("789765445whjdbjwhwfbs977865"))   # bbdfhhjjswww446688555777799
