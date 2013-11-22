#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def to_csv(s):
  results = []
  str_token = []
  for t in s.split(","):
    try:
      # Int?
      results.append(int(t))
    except:
      # String
      str_token.append(t)
      if t[-1] == '"':
        result = ",".join(str_token)
        # Remove unneeded apostrophes
        results.append(result[1:-1])
        str_token = []
  return results

print to_csv('2,6,3,2,5')
print to_csv('"pears","apples","walnuts","grapes","cheese,cake"')
print to_csv('1,"Que?","Kay?",2,"Si.","Sea? Kay, sea?","No, no, no. Que...  ‘what’.", \
             234,"Kay Watt?","Si, que ‘what’.","C.K.  Watt?",3,"Yes!","comma,comma, comma , :)"')
