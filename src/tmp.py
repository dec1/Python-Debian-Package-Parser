#  # pick combinations of K squares from those in field
#  # for each comb, c
#       find sequence from start -> finish
#         lc = length of this sequence
#     find average of lc for all combs
#
#
#
# Explanation:
# Let (i,j) be the square represented by the j-th character of the i-th element of field (both numbers are 0-based).
#
# . passable
# * checkpoint (and passable)
# # impass
# - invalid
#
# K num of checkpoints chosen (randomly)
#
#
# field = [
#  "*#..#",
#  ".#*#.",
#  "*...*"]
# K = 2
#
#
#
# If she chooses (0,0) and (1,2),   one of the optimal sequences is (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (1,2).
# If she chooses (0,0) and (2,0),   one of the optimal sequences is (0,0) -> (1,0) -> (2,0).
# If she chooses (0,0) and (2,4),   one of the optimal sequences is (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (2,3) -> (2,4).
# If she chooses (1,2) and (2,0),   one of the optimal sequences is (1,2) -> (2,2) -> (2,1) -> (2,0).
# If she chooses (1,2) and (2,4),   one of the optimal sequences is (1,2) -> (2,2) -> (2,3) -> (2,4).
# If she chooses (2,0) and (2,4),   one of the optimal sequences is (2,0) -> (2,1) -> (2,2) -> (2,3) -> (2,4).
# If she chooses (0,0), (1,2), and (2,4)  # ?? not clear if perm or comb needed  - presume comb for now
#  # but leave extendable (for two reverse path would have been only alt and it has same length - for 2+ you can have different 'sequences' that would yield different lengths
#
# So the expected length of her sequences is:
#   (5 + 2 + 6 + 3 + 3 + 4) / 6 = 23 / 6 = 3.8333333333333353
from typing import List


def elem(i:int, j:int, field: List[str]) -> str:
  row_cnt = len(field)
  if i-1 > row_cnt:
    print(f"index out of range looking for row {i} in field with {row_cnt} rows")
    return "-"

  row = field[i]

  col_cnt = len(row)
  if j-1 > col_cnt:
    print(f"index out of range looking for elem {j} in row with {col_cnt} elems")
    return "-"

  elem = row[j]
