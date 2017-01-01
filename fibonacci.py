"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position == 0: return 0
    if position == 1: return 1
    return get_fib(position - 1) + get_fib(position - 2)

# Test cases
#print 'With recursive method:'
print get_fib(9)
print get_fib(11)
print get_fib(0)


# Here's the iterative method
def get_fib(position):
    if position == 0: return 0
    if position == 1: return 1
    first = 0
    second = 1
    next = first + second
    for i in range(2, position):
        first = second
        second = next
        next = first + second
    return next
        
# Test cases
#print 'With iterative method:'
print get_fib(9)
print get_fib(11)
print get_fib(0)
