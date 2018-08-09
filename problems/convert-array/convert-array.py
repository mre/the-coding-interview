def convert_array(arr):
    """
    In-place algorithm without using extra space
    """
    size = len(arr) // 3
    for idx in range(len(arr)):
        swap_index = (idx % 3) * size + (idx // 3)
        while swap_index < idx:
            swap_index = (swap_index % 3) * size + (swap_index // 3)
        arr[idx], arr[swap_index] = arr[swap_index], arr[idx]
    return arr

print(convert_array(["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"])) # ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']
print(convert_array(["a1", "a2", "a3", "a4", "b1", "b2", "b3", "b4", "c1", "c2", "c3", "c4"])) # ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3', 'a4', 'b4', 'c4']
print(convert_array(["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "c1", "c2", "c3", "c4", "c5"])) # ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3', 'a4', 'b4', 'c4', 'a5', 'b5', 'c5']
