lawn = ["1144144", "1144144", "1122122", "9999999"]
heights = [max(line) for line in lawn]
max_line = heights.index(max(heights))
print lawn[max_line]
