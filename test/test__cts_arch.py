"""  CtsArch tests """

from src._cts_arch import CtsArch
from src._man_file import ManFile


def test_top_pkgs_from_file():
    """ Test CtsArch.test_top_pkgs_from_file() """

    expect = [('p2', 3), ('p1', 2), ('p3', 1)]

    file_path = ManFile.file_path_fixture("Contents-simple")
    res = CtsArch._top_pkgs_from_file(file_path=file_path, max_pkgs=4)  # pylint: disable=protected-access

    assert res == expect
