# brute force implementation
def find_duplicate_element_brute_force(elements):
    for id, element in enumerate(elements):
        if(id+1 == len(elements)):
            return None
        for second_element in elements[id+1:]:
            if element == second_element:
                return element
    return None

# hash implementation
def find_duplicate_element_hash(elements):
    element_dict = {}

    for element in elements:
        if element in element_dict.keys():
            return element
        else:
            element_dict[element] = 1
    return None

# sort implementation
def find_duplicate_element_sort(elements):
    elements.sort()
    for id, element in enumerate(elements):
        if id+1 == len(elements):
            return None
        if(element == elements[id+1]):
            return element
    return None

# binary search, recursive implementation
def find_duplicate_element_binary_search(elements):
    if(len(elements) < 2): return None
    if(max(elements)+1 != len(elements)): return None

    return find_duplicate_element_binary_search_r(elements, 1, len(elements) - 1)

def find_duplicate_element_binary_search_r(elements, low_value, high_value):
    if(low_value == high_value):
        return high_value

    midpoint = int((high_value+low_value)/2)
    low_count = 0

    for element in elements:
        if (element <= midpoint) and (element >= low_value):
            low_count = low_count +1

    if low_count > midpoint - low_value +1:
        return find_duplicate_element_binary_search_r(elements, low_value, midpoint)
    else:
        return find_duplicate_element_binary_search_r(elements, midpoint+1, high_value)


#NOTE: This solution contains several implementations. See hints in problem description for explanation
functions = [
    find_duplicate_element_brute_force,
    find_duplicate_element_hash,
    find_duplicate_element_sort,
    find_duplicate_element_binary_search]

for find_duplicate_element_function in functions:
    print "function: ", find_duplicate_element_function
    elements = [9, 8, 6, 7, 5, 7, 3, 4, 2, 1]
    assert(find_duplicate_element_function(elements) == 7)

    assert(find_duplicate_element_function([1,2,2]) == 2)
    assert(find_duplicate_element_function([]) == None)
    assert(find_duplicate_element_function([1]) == None)
    assert(find_duplicate_element_function([1,2,3]) == None)
