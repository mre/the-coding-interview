def split_string(string, delimiter):
    words = []
    current_word = ""
    for char in string:
        if char == delimiter:
            words.append(current_word)
            current_word = ""
        else:
            current_word += char
    words.append(current_word)
    return words

print(split_string("hello, world", ",")) # ['hello', ' world']
print(split_string("hello  world", ",")) # ['hello  world']
print(split_string("", ",")) # ['']
