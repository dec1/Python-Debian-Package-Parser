""" ManFile tests """

import os
from src._man_file import ManFile


# ---------------------------------------------------------
def test_full_path():
    """ test full_path() """

    # Helper to create OS-specific paths (e.g., /b vs \b)
    def p(path_str):
        return path_str.replace("/", os.sep)

    assert ManFile.full_path(rel_path="f", root_path="b") == os.path.join("b", "f")

    # Updated assertions to use OS-specific separators for Windows compatibility
    assert ManFile.full_path(rel_path="f", root_path=p("/b")) == os.path.normpath(p("/b/f"))
    assert ManFile.full_path(rel_path="f", root_path=p("/b/c")) == os.path.normpath(p("/b/c/f"))

    # FIX: Wrap "f1/f2" in p() so it becomes "f1\f2" on Windows before joining
    assert ManFile.full_path(rel_path=p("f1/f2"), root_path=p("/b/c")) == os.path.normpath(p("/b/c/f1/f2"))


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