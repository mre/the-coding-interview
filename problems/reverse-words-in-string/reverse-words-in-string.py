import re

def reverse_str(string):
    string = string.strip()
    string = re.sub("\s+", " ", string)
    result = [word[::-1] for word in string[::-1].split(" ")]
    return " ".join(result)

# "degree CS":
print reverse_str("   CS degree")
print reverse_str("CS    degree")
print reverse_str("CS degree   ")
print reverse_str("   CS   degree") 

