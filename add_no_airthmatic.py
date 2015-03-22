# PROBLEM: WRITE A FUNCTION THAT ADDS TWO NUMBERS. YOU SHOULD NOT USE + OR ANY
# ARITHMETIC OP- ERATORS.
#
# Authod: Milad Mohammadi

def add_no_arithmatic (a, b):
    if b == 0: return a
    sum_val = a ^ b
    carry_val = (a & b) << 1
    return add_no_arithmatic (sum_val, carry_val)

print add_no_arithmatic (12, 40)
