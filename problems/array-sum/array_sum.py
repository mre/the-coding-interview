# Using Recursion

sum_arr = 0 # Global Sum variable.

def sum_of_array(a):
    global sum_arr
    for i in a:
        if type(i) != list: # Check if i is a list or not
            sum_arr += i 
        else:
            sum_of_array(i) # Recursive call to function if i is a list
    return sum_arr


arr = [[1],[2],[3,4,[5]]]
print(sum_of_array(arr))