# encoding: utf-8
"""
Function that receives an array of single digit ints representing a longer
integer, such as [8, 7, 9, 9] representing 8,799, and increments it by 1
returning the result also in an array format.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2010
"""

def increment(input_list):
    i = len(input_list) - 1
    carry = 1
    while i >= 0:
        value = input_list[i]
        new_value = value + carry
        if 10 - new_value == 0:
            carry = 1
            input_list[i] = 0
        else:
            carry = 0
            input_list[i] = new_value
        i -= 1
        if not carry:
            break
    if carry:
        input_list.insert(0, carry)
    return input_list


