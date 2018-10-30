def split_string(string: str, delimiter):
    return string.split(delimiter)

a = 'hello , word'
print(split_string(a," "))  #['hello', ',', 'word']
