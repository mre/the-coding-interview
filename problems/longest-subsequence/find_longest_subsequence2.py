def find_longest_subsequence(integers):
  runs = defaultdict()
  for i in integers:
    if i-1 in runs.keys():
      run = runs[i-1]
      run.append(i)
    if i+1 in runs.keys():
      run = runs[i+1]
      run.append(i)
  print runs


find_longest_subsequence([1,2,3,4,7,5,12,13])
