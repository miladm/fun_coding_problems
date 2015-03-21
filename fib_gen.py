# PROBLEM:
#  Write a method to generate the nth Fibonacci number.
#
# Author: Milad Mohammadi

def get_nth_fib (n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 1
    else:
        n_0 = 0
        n_1 = 1
        n_2 = 1
        for i in xrange(2,n):
            n_0 = n_2 + n_1
            n_2 = n_1
            n_1 = n_0
        return n_0

print get_nth_fib (7)
