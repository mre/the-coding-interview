def array_sum(arr):
    sum = 0
    for item in arr:
        if isinstance(item, list):
            sum = sum + array_sum(item)
        else:
            sum = sum + item
    return sum

print array_sum([1,2,[3,4,[5]]])

# Array sum (without recursion)
def array_sum(arr):
    """
    1. Converts the array into the string and removes characters - '[', ']'
    2. Splits on commas (',') to get the list of integers
    3. Sums the integers up
    """
    sum = 0
    arr = str(arr)
    arr = arr.replace('[', '').replace(']', '').split(',')
    for i in arr:
        if i.strip().isdigit():
            sum += int(i)
    return sum

print(array_sum([1,2,[3,4,[5,3,3,213123,345345], [[[1,[1000,[1010]]]]]]])) # 560500
print(array_sum([1,2,[3,4,[5]]])) # 15
print(array_sum([1,2,3, [4,5,6], [7,8,9], [10,11,12,[13,14,15,[16,17,18,[19,[20]]]]]])) # 210
