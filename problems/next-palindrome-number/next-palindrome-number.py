from random import randint

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def next_palindrome_brute(n):
    while not is_palindrome(n+1):
        n += 1
    return n + 1


def even(n):
    return n % 2 == 0

def next_palindrome(n):
    digits = str(n)
    if even(n):

        palindrome = 
    else:



r = randint(1,99999999)
print r, next_palindrome(r)
