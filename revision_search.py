# PROBLEM:
#  YOU ARE GIVEN A STRING SVN REVISION NUMBERS. YOU ARE ASKED TO FIND THE FIRST
#  BAD REVISION IN THE SEQUENCE. THE REVISION NUMBERS INTERVAL IS PROVIDED AS
#  TWO NUMBERS SPECIFIYING THE HEAD AND TAIL OF THE SEQUENCE. YOU ARE PROVIDED
#  WITH A FUNCTION, CALLED isRevGood(<rev_id>), DETERMINING THE GOODNESS OF THE
#  REVISION NUMBER
#
# Author: Milad Mohammadi

def findBadRevision (x, y):
  rev_range = y - x + 1
  mid = rev_raneg / 2 + x

  if rev_range > 2:
    if !isRevGood (mid):
      return findBadRevision (x, mid)
    else:
      return findBadRevision (mid, y)
  else:
    return y

# THE SPACE COMPLEXITY OF THIS PROBLEM IS O(1) WHILE ITS TIME COMPLEXITY IS
# O(logn)
