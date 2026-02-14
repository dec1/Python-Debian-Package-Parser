""" test/test__man_web.py """

import gzip
from src._man_web import ManWeb


# ---------------------------------------------------------
def test_download_cts(tmpdir):
    """ test download() with a (binary gz) file"""

    # note: pytest "tmpdir"  fixture automatically passed here, as base "dir_path",

    remote_file = "Contents-udeb-all.gz"

    # manually calculated md5 - REMOVED (content changes too often)
    # md5_expect = "ee895dbd9bd48003612c5a76202f7dce"

    url = ManWeb.full_path(rel_path=remote_file)
    file_path = ManWeb.download(url, tmpdir)

    # Verify the file is a valid GZIP file instead of checking hash
    try:
        with gzip.open(file_path, 'rb') as f:
            f.read(1)
    except (OSError, gzip.BadGzipFile) as e:
        assert False, f"Downloaded file is not a valid GZIP: {e}"


# ---------------------------------------------------------
def test_download_listing(tmpdir):
    """ test download() with a (text) listing file"""

    remote_file = ""

    # manually calculated md5 - REMOVED (content changes too often)
    # md5_expect = "04d7ec8802dc45f5a2818380fb37345e"

    # expect page to contain this text
    substr_expected = "Index of /debian/dists/stable/main"

    url = ManWeb.full_path(rel_path=remote_file)
    file_path = ManWeb.download(url, tmpdir)

    # md5 = ManUtil.md5_hash(file_path)

    with open(file_path, encoding='utf-8') as file:
        txt = file.read()
        assert substr_expected in txt

    # assert md5.strip() == md5_expect.strip()
