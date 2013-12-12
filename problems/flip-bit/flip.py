def flip(integer, bit):
  return integer ^ (1 << (bit - 1))

print flip(8, 3) # 12
print flip(8, 4) # 0
