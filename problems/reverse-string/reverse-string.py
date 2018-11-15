def reverse_string(string):
    return string[::-1]

def reverse_string2(string):
    return "".join(reversed(list(string)))

def reverse_string3(string):
    res = ""
    for ch in string:
        res = ch + res
    return res
  
def reverse_string4(string):
  from functools import reduce
  return reduce(lambda a,x: a+x, reversed(string))


assert(reverse_string("hello world") == "dlrow olleh")

assert(reverse_string2("hello world") == "dlrow olleh")

assert(reverse_string3("hello world") == "dlrow olleh")
