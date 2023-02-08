"""  ManApp tests """

from src._man_app import ManApp


def test__arch_from_parms():
    """ test processing of command line parameters """
    arch = "i386"
    ret = ManApp._arch_name_from_parms([arch])  # pylint: disable=protected-access
    assert ret == arch


# -----------------------------------------------------------
def test__arch_stats_str():
    """ integration test : report of package statistics """

    arch = "udeb-all"
    ret = ManApp.arch_stats_str([arch])

    expect = """\
|  1 | debian-installer/xkb-data-udeb                     |         293 |
|  2 | debian-installer/fonts-noto-unhinted-udeb          |         270 |
|  3 | debian-installer/ca-certificates-udeb              |         259 |\
"""

    assert ret
    assert expect in ret


# -----------------------------------------------------------
def test__arch_stats_str_fail():
    """ test behaviour when passed invalid package name """

    arch = "doesnt_exist"
    ret = ManApp.arch_stats_str([arch])

    assert not ret
