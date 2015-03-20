#PROBLEM STATEMENT:
#DESIGN AN ALGORITHM AND WRITE CODE TO FIND THE FIRST COMMON ANCESTOR OF TWO
#NODES IN A BINARY TREE. AVOID STORING ADDITIONAL NODES IN A DATA STRUCTURE.
#NOTE: THIS IS NOT NECESSARILY A BINARY SEARCH TREE.
#
# Author: Milad Mohammadi

import sorted_array_to_bst

def get_common_ancestor (node, A, B):
    if node == None: return None

    if node.val == A or node.val == B:
        return node.val
    else:
        left_val = get_common_ancestor (node.left, A, B)
        right_val = get_common_ancestor (node.right, A, B)

        if left_val == None and right_val == None: return None
        elif left_val == None: return right_val
        elif right_val == None: return left_val
        else: return node.val


test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
root = sorted_array_to_bst.sorted_array_to_bst (test)
print 'Common ancestor:', get_common_ancestor (root, 6, 9)
