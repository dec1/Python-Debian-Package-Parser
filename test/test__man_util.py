""" ManUtil tests """

from src._man_util import ManUtil
from src._man_file import ManFile


def test_unzip(tmpdir):
    """ test unzip() """

    file_name = "Contents-udeb-all.gz"

    # manually calculated md5 for (unzipped) 'Contents-udeb-all'
    md5_expect = "1f4bf598c355a2bbb0c8ddf889d9636e"

    file_path_src = ManFile.file_path_fixture(file_name)
    file_path_dst = ManFile.full_path(root_path=tmpdir, rel_path=file_name)

    assert ManFile.path_exists(file_path_src)

    ManFile.path_ensure_remove(file_path_dst)
    assert not ManFile.path_exists(file_path_dst)

    ManUtil.unzip(file_path_src=file_path_src, file_path_dst=file_path_dst)

    assert ManFile.path_exists(file_path_dst)

    md5 = ManUtil.md5_hash(file_path_dst)
    assert md5 == md5_expect


# --------------------------------------------
def test_hash():
    """ test md5_hash() """

    file_name = "Contents-udeb-all.gz"

    # manually calculated md5 for 'Contents-udeb-all.gz'
    md5_expect = "708ed31f29f9daf4c980b7abdd66c356"

    file_path = ManFile.file_path_fixture(file_name)
    md5 = ManUtil.md5_hash(file_path)

    assert md5 == md5_expect
