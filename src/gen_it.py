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
from typing import Tuple

# ---------------------------------------
# ---------------------------------------
def elem_at_move(i:int, j:int, i_inc: int, j_inc:int, field: List[str]) -> str:
    """ element at position (i + i_inc, j + j_inc of field)
    """

    square = elem(i + i_inc, j + j_inc, field)
    return square

# ---------------------------------------
def elem(i:int, j:int, field: List[str]) -> str:
    """ element at position (i,j)
         i, j are zero based and top left is (0,0)
    """
    row_cnt = len(field)
    if i < 0 or (i - 1 > row_cnt):
        print(f"index out of range looking for row {i} in field with {row_cnt} rows")
        return "-"

    row = field[i]

    col_cnt = len(row)
    if j < 0 or (j - 1 > col_cnt):
        print(f"index out of range looking for elem {j} in row with {col_cnt} elems")
        return "-"

    elem = row[j]
    return elem

# ------------------------------------------------------------------
def moves_valid(i:int, j:int, field: List[str]) -> List[Tuple[int,int]]:
    """ moves but without including impassable '#' squares
    """
    moves_all = moves(i,j, field)
    ret = []
    for move in moves_all:
        inc_i = move[0]
        inc_j = move[1]
        square = elem_at_move(i,j, inc_i, inc_j, field)
        if square == "*" or square == ".":
            ret.append(move)


    return ret

# ---------------------------------------
def moves(i:int, j:int, field: List[str]) -> List[Tuple[int,int]]:
    """  neighbouring squares that player can move to from (i, j) in single step
            without leaving field
    """
    row_cnt = len(field)
    if row_cnt < 1:
        print(f"unexpected empty field in moves({i},{j})")
        return []

    # append increments that dont move outside field (ie from (i0,j0) on border)
    my_incs = []
    if i > 0:
        my_incs.append((-1, 0))
    if i < row_cnt-1:
        my_incs.append((1, 0))

    row = field[i]
    col_cnt = len(row)
    if col_cnt < 1:
        print(f"unexpected empty col in moves({i},{j})")
        return []

    if j > 0:
        my_incs.append((0, -1))
    if j < row_cnt-1:
        my_incs.append((0, 1))


    return my_incs


# ---------------------------------------

def seqs(i0: int, j0: int, i1: int, j1: int, field: List[str]) -> List[List[Tuple[int, int]]]:
    """ valid (dont cross border and dont pass '#') seq from (i0,j0) -> (i1,j1) of field

    """
 # todo - finish implementing (recursive) pseudocode for calculating valid sequences from src (i0,j0) -> (i1,j1) :
 # for each valid (one step move) of moves (that dont take you over boundary or across '#', from square
    # see if you have (already) reached dst (ie i1,j1)
    #   for each other move: recurse

# implementation:
# have 'node' classes ~ square (i, j) on field
# each node has a list of valid (without crossing boundary or '#') "next step" nodes that can be moved to from there
# one of these is also "prev step" that

# a sequence is a list of nodes (each with node of list only contained once)
#  with start node  (i1,j1):
#    for a node:
#       fill out "prev step" the "next step nodes"
#           excluding:
#               "prev step" from "next step nodes" so cant backtrack
#               and any node that can be found when following up to parent (start node) directly
#           recurse (ie for each "next step nodes") call recursively, in turn filling out their
#               "prev step" and "next step nodes"
#               rercursion ends when target (ie i1,j1) has been reached - save path (back to start node) in separate
#                   seqs variable to be returned at end of fun
#               or more next step nodes available that arent excluded as per above


    return []
  # ---------------------------------------
if __name__ == "__main__":
    halt = 1
    #  todo:
    #  finish implementing algorithm in seqs() - described in pseudocode there
    #  prune any of these seqs that dont contain K of '*'
    #      it could be computationally more efficient to do this in the calculation of seqs already.
    #      however it makes the solution less extensible and flexible - maybe conditions needs be altered or some other contidion needs to be added later?
    #      making these changes inside seq() is more difficult and error prone- whoever makes this change has to fully understand the rest of implementation of seqs() and not break it
    #      so this is a trade off between performane and
    # calculate average path length from this
