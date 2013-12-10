import pyenchant

def words(board):
  d = enchant.Dict("en_US")
  print d.check("Hello")
  print d.check("Helo")
