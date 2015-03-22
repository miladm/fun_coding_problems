# PROBLEM:
#   GIVEN AN INPUT STRING AND A REGULAR EXPRESSION STRING THAT CONSISTS OF
#   NUMBERS, LETTERS, '.', NAD '*', FIND IF THE INPUT MATCHES THE REGULAR
#   EXPRESSION.
#
# Author: Milad Mohammadi

def match (regex, in_str):
  if len (regex) == 0:
      return True
  if len (in_str) == 0:
      return False

  if len (regex) == 1:
    if regex[0] != '.' and regex[0] == in_str[0]:
      return True
    if regex[0] != '.' and regex[0] != in_str[0]:
      return False
    if regex[0] == '.':
      return True

  if regex[1] != '*':
    if regex[0] != '.' and regex[0] != in_str[0]:
      return False
    else:
      return match (regex [1:], in_str[1:])
  else:
    if match (regex[2:], in_str[:]): # WHEN LENGTH OF * IS ZERO
      return True
    for p in xrange (len (in_str)):
      if regex[0] != '.':
        if regex[0] == in_str[p] and p > 0:
          if match (regex[2:], in_str[p:]):
            return True
      else:
        if p > 0:
          if match (regex[2:], in_str[p+1:]):
            return True
    return False



regex = 'ada*c*.*dk'
in_str = 'adaaaadzzzdk'

print '\n**', in_str, 'AND', regex, 'MATCH?'
print match (regex, in_str), '\n'
