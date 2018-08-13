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

print(substrings("abc"))

# Another approach
def substrings(string):
  return [string[i:j+1] for i in range(len(string)) for j in range(i,len(string))]

print(substrings("abc")) # ['a', 'ab', 'abc', 'b', 'bc', 'c']
