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

