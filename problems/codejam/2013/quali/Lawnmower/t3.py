"""
31:


1222222
2222222
2222222
2222222
2222222
"""


def below_max_height(lawn, max_height = 100):
  for line in lawn:
    if any(1 <= field <= max_height for field in line):
      return "NO"
  return "YES"

def solve(lawn):
  # Take highest setting as pattern
  heights = [sum(int(i) for i in line) for line in lawn]
  max_line = heights.index(max(heights))
  pattern = lawn[max_line]

  # Check all other lines against this pattern
  other_lines = lawn[:max_line] + lawn[max_line+1:]
  print pattern
  for line in other_lines:
    print line
    if line != pattern:
      setting = max(line)
      trimmed = [min(setting, p) for p in pattern]
      print trimmed
      if line != trimmed:
        return "NO"
  return below_max_height(lawn)

board = ["1111", "2221", "2222"]

print solve(board)
