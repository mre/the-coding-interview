def convert_array(arr):
    if len(arr) % 3 != 0:
        return
    result = []
    slice = len(arr)/3
    for i in range(slice):
        result.extend([arr[i], arr[slice + i], arr[2*slice + i]])
    return result

print convert_array(["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"])
