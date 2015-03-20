#PROBLEM STATEMENT:
# GIVEN A SORTED (INCREASING ORDER) ARRAY, WRITE AN ALGORITHM TO CREATE A BINARY
# TREE WITH MINIMAL HEIGHT.
# 
# Author: Milad Mohammadi

class bst_node:
    def __init__ (self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst (A):
    if len(A) == 0: return None
    mid_indx = len(A) / 2
    mid = A[mid_indx]
    node = bst_node (mid, None, None)
    print node.val
    if len(A) == 1:
        return node
    elif len(A) == 2:
        node.left = bst_maker (A[0:1])
    else:
        node.left = bst_maker (A[0:mid_indx])
        node.right = bst_maker (A[mid_indx+1:])
    return node


test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sorted_array_to_bst (test)
