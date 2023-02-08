""" ManWeb tests """

from src._man_web import ManWeb
from src._man_util import ManUtil


# ---------------------------------------------------------
def test_full_path():
    """ test full_path() """

    assert ManWeb.full_path(rel_path="f1", base_path="dir") == "dir/f1"
    assert ManWeb.full_path(rel_path="/f1", base_path="dir") == "dir/f1"


# ---------------------------------------------------------
def test_download_cts(tmpdir):
    """ test download() with a (binary gz) file"""

    # note: pytest "tmpdir"  fixture automatically passed here, as base "dir_path",

    remote_file = "Contents-udeb-all.gz"

    # manually calculated md5
    md5_expect = "708ed31f29f9daf4c980b7abdd66c356"

    url = ManWeb.full_path(rel_path=remote_file)
    file_path = ManWeb.download(url, tmpdir)

    md5 = ManUtil.md5_hash(file_path)
    assert md5 == md5_expect


# ---------------------------------------------------------
def test_download_listing(tmpdir):
    """ test download() with a (text) listing file"""

    remote_file = ""

    # manually calculated md5
    md5_expect = "e08ba6e440971b60b54462767fca0cc9"

    # expect page to contain this text
    substr_expected = "Index of /debian/dists/stable/main"

    url = ManWeb.full_path(rel_path=remote_file)
    file_path = ManWeb.download(url, tmpdir)

    md5 = ManUtil.md5_hash(file_path)
    with open(file_path, encoding='utf-8') as file:
        txt = file.read()
        assert substr_expected in txt
    assert md5 == md5_expect


# ---------------------------------------------------------
def test_url_ensure_absolute():
    """ test durlbase() """

    base = ManWeb.urlbase()
    file = "my_file"
    full = ManWeb.full_path(base_path=base, rel_path=file)

    assert ManWeb.ensure_absolute(file) == full
    assert ManWeb.ensure_absolute(full) == full
