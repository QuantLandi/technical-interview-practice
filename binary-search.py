"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

import math

def binary_search(input_array, value):
    """Your code goes here."""
    sublist = input_array
    iterations = range(0, int(math.ceil(math.log(len(input_array), 2))))
    for _ in iterations:
        middle_value_ix = len(sublist) / 2
        middle_value = sublist[middle_value_ix]
        if middle_value == value:
            return input_array.index(value)
        else:
            if value > middle_value:
                sublist = sublist[middle_value_ix + 1:]
            else:
                sublist = sublist[:middle_value_ix]
    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
