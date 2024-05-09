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
    assert ret
    expect = """\
|    | Package                                            |   Num Files |
|---:|:---------------------------------------------------|------------:|
|  1 | debian-installer/xkb-data-udeb                     |         292 |
|  2 | debian-installer/ca-certificates-udeb              |         281 |
|  3 | debian-installer/fonts-noto-unhinted-udeb          |         270 |
|  4 | debian-installer/console-keymaps-at                |         128 |
|  5 | debian-installer/debootstrap-udeb                  |          80 |
|  6 | debian-installer/console-keymaps-acorn             |          57 |
|  7 | debian-installer/console-setup-linux-charmaps-udeb |          56 |
|  8 | debian-installer/kickseed-common                   |          40 |
|  9 | debian-installer/debian-edu-profile-udeb           |          36 |
| 10 | debian-installer/console-setup-freebsd-fonts-udeb  |          36 |\
"""



    assert expect in ret


# -----------------------------------------------------------
def test__arch_stats_str_fail():
    """ test behaviour when passed invalid package name """

    arch = "doesnt_exist"
    ret = ManApp.arch_stats_str([arch])

    assert not ret
