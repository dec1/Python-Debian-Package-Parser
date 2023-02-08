""" Gen_It tests """

from src.gen_it import elem, moves, moves_valid

# --------------------------------------------
def test_moves_valid():
    """ test test_moves_valid() """
    field = [
    "*#..#",
    ".#*#.",
    "*...*"]

    assert moves_valid(1,0, field) == [(-1, 0), (1, 0)]

    field = [
    "##..#",
    ".#*#.",
    "*...*"]

    assert moves_valid(1,0, field) == [ (1, 0)]


# --------------------------------------------
def test_moves():
    """ test moves() """

    field = [
        "*#..#",
        ".#*#.",
        "*...*"]

    # border cases
    assert moves(0, 0, field) == [(1, 0), (0, 1)]
    assert moves(2, 4, field) == [(-1, 0), (0, -1)]

    # non-border - expect 4
    assert moves(1, 1, field) ==  [(-1, 0), (1, 0), (0, -1), (0, 1)]

# ---------------------------------------------------------
def test_elem():
    """ test full_path() """

    field = [
    "*#..#",
    ".#*#.",
    "*...*"]



    assert elem( 1,1, field) == "#"
    assert elem(0,0, field) == "*"

    # expect 'fail'
    assert elem(5, 1, field) == "-"
    assert elem(-1, -1, field) == "-"
