"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if array == []: return []
    first_ix = 0
    first = array[first_ix]
    pivot_ix = len(array) - 1
    pivot = array[pivot_ix]
    before_pivot = array[pivot_ix - 1]
    while first_ix < pivot_ix:
        if first > pivot:
            array[pivot_ix] = first
            array[first_ix] = before_pivot
            array[pivot_ix - 1] = pivot
            pivot_ix -= 1
            first = array[first_ix]
            before_pivot = array[pivot_ix - 1]
        else:
            first_ix += 1
            first = array[first_ix]
    return quicksort(array[:pivot_ix]) + \
           [array[pivot_ix]] + \
           quicksort(array[pivot_ix + 1:])


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)


#    print 'first_ix: {}, first: {}, pivot_ix: {}, pivot: {}, second: {}'.\
#    format(first_ix, first, pivot_ix, pivot, second)
#    print array

#    print array
#    print pivot_ix, array[:pivot_ix], array[pivot_ix + 1:]
    
