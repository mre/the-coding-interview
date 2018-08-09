def flatten(arr):
    result = []
    for i in arr:
        try:
            if len(i):
                result.extend(flatten(i))
        except:
            result.append(i)
    return result

print flatten([1, 2, [3, [4], 5, 6], 7]) # [1, 2, 3, 4, 5, 6, 7]


# Another way of doing it using string conversion
# Note that it returns the same 'arr' instance without creating a new list
def flatten(arr):
    """
    1. Converts the array into the string and removes characters - '[', ']'
    2. Splits on commas (',') to get the list of integers
    3. Removes the trailing whitespaces (in python, elements of the list are separated by comma + space)
    4. Modifies the elements of the initial array
    """
    arr = str(arr)
    arr = arr.replace('[', '').replace(']', '').split(',')
    for i in range(len(arr)):
        if arr[i].strip().isdigit():
            arr[i] = int(arr[i])
    return arr

print(flatten([1, 2, [3, [4], 5, 6], 7, [8, 9, [10, 11, [12, [13, 14]]]]])) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
