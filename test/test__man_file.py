""" ManFile tests """

import os
from src._man_file import ManFile


# ---------------------------------------------------------
def test_full_path():
    """ test full_path() """

    assert ManFile.full_path(rel_path="f", root_path="b") == "b/f"
    assert ManFile.full_path(rel_path="f", root_path="/b") == "/b/f"
    assert ManFile.full_path(rel_path="f", root_path="/b/c") == "/b/c/f"
    assert ManFile.full_path(rel_path="f1/f2", root_path="/b/c") == "/b/c/f1/f2"


# ---------------------------------------------------------
def test_dir_path_root():
    """ test dir_path_root() """

    path = ManFile.dir_path_root()

    assert os.path.exists(path)
    assert os.path.isdir(path)

    contents = os.listdir(path)
    assert "src" in contents
    assert "prj" in contents


# ---------------------------------------------------------
def test_dir_path_fixture():
    """ test dir_path_fixture() """

    path = ManFile.dir_path_fixture()

    assert os.path.exists(path)
    assert os.path.isdir(path)

    contents = os.listdir(path)
    assert "Contents-udeb-all" in contents
