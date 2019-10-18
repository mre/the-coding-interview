def largest_palindrome(string):
    """
    Runtime: O(
    """
    max_len = len(string)+1
    # Begin with the largest possible palindrome
    for length in range(max_len,0,-1):
        start = 0
        end = length
        while (end < max_len):
            curr = string[start:end]
            rev = curr[::-1]
            if curr == rev:
                return curr
            start += 1
            end += 1
    # Return an empty string if the input was empty
    return ""


print largest_palindrome("I am a red racecar driver")
print largest_palindrome("reliefpfeiler") # Largest German palindrome
print largest_palindrome("ein neger mit gazelle zagt im regen nie") # Largest German palindrome
print largest_palindrome("einnegermitgazellezagtimregennie") # Largest German palindrome
