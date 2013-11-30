def selection_sort(unsorted_list):
    sorted_list = []
    while unsorted_list:
        minimum = min(unsorted_list)
        unsorted_list.remove(minimum)
        sorted_list.append(minimum)
    return sorted_list

print selection_sort([1,25,67,32,2,4,6,7,8,4,3,32,1,32])
