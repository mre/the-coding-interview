# encoding: utf-8
"""
Find the longest subsequence of consecutive integers.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""


def find_longest_subsequence_with_sorting(input_array):
    """Solution: O(n log(n))"""
    input_array.sort()
    longest_sequence = []
    i = 0
    running_sequence = [input_array[i]]

    while i < len(input_array) - 1:
        next = i + 1
        if input_array[next] - input_array[i] == 1:
            running_sequence.append(input_array[next])
            if len(running_sequence) > len(longest_sequence):
                longest_sequence = running_sequence
        else:
            running_sequence = [input_array[next]]
        i += 1
    return longest_sequence


def find_longest_subsequence(input_array):
    """Solution O(n)"""
    input_set = set(input_array)
    longest_sequence = []

    while input_set:
        element = input_set.pop()

        smaller_element = element - 1
        while smaller_element in input_set:
            input_set.remove(smaller_element)
            smaller_element -= 1

        larger_element = element + 1
        while larger_element in input_set:
            input_set.remove(larger_element)
            larger_element += 1

        current_sequence = range(smaller_element + 1, larger_element)
        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
    return longest_sequence
