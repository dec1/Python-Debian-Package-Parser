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

    # Normalize result to replace non-breaking spaces with standard ASCII spaces
    # and handle potential variations in mirror data by checking for package presence
    clean_ret = ret.replace('\u00a0', ' ')

    # Check for the presence of the header and key package names
    # expected to be in the top results for udeb-all
    assert "Package" in clean_ret
    assert "Num Files" in clean_ret
    assert "debian-installer/xkb-data-udeb" in clean_ret
    assert "debian-installer/ca-certificates-udeb" in clean_ret


# -----------------------------------------------------------
def test__arch_stats_str_fail():
    """ test behaviour when passed invalid package name """

    arch = "doesnt_exist"
    ret = ManApp.arch_stats_str([arch])

    assert not ret
