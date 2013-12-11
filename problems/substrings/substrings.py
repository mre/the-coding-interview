def substrings(string):
  result = [string]
  for length in range(1, len(string)):
    start = 0
    end = start + length
    while end <= len(string):
      result.append(string[start:end])
      start += 1
      end   += 1
  return result

print substrings("abc")
