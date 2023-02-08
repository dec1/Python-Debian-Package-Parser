""" ManParser tests """

from src._man_parser import ManParser


# -----------------------------------------------
def _listing_str():
    """ fixture used in tests below """

    # pylint: disable-next=line-too-long
    ret = """
    <html data-lt-installed="true"><head>
    <meta http-equiv="content-type" content="text/html; charset=windows-1252"><title>Index of /debian/dists/stable/main/</title></head>
    <body>
    <h1>Index of /debian/dists/stable/main/</h1><hr><pre><a href="http://ftp.uk.debian.org/debian/dists/stable/">../</a>
    <a href="http://ftp.uk.debian.org/debian/dists/stable/main/binary-all/">binary-all/</a>                                        10-Sep-2022 10:18                   -
    <a href="http://ftp.uk.debian.org/debian/dists/stable/main/i18n/">i18n/</a>                                              10-Sep-2022 10:18                   -
    <a href="http://ftp.uk.debian.org/debian/dists/stable/main/Contents-all.gz">Contents-all.gz</a>                                    10-Sep-2022 09:48            31026385
    <a href="http://ftp.uk.debian.org/debian/dists/stable/main/Contents-i386.gz">Contents-i386.gz</a>                                   10-Sep-2022 09:47            10206461
    </pre><hr>
    </body></html>
    """

    return ret


# ------------------------------------------------------------------------------
def test_parse_listing():
    """  verify that fixture gets (initially) parsed (as dict) """
    expect = {
        'Contents-all.gz': 'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-all.gz',
        'Contents-i386.gz': 'http://ftp.uk.debian.org/debian/dists/stable/main/Contents-i386.gz',
    }

    dict_got = ManParser.parse_listing(_listing_str())

    assert dict_got == expect


# ------------------------------------------------------------------------------
def _test_parse_cts_line(txt: str, expect):
    ret = ManParser.parse_cts_line(txt)
    assert ret == expect


# ------------------------------------------------------------------------------
def test_parse_cts_line():
    """ Test ManParser.parse_cts_line() """

    # file with path
    _test_parse_cts_line(txt="bin/netcfg    debian-installer/netcfg,debian-installer/netcfg-static",
                         expect=("bin/netcfg", ["debian-installer/netcfg",
                                                "debian-installer/netcfg-static"]))  # pylint: disable=line-too-long

    # file no path
    _test_parse_cts_line(txt="netcfg       debian-installer/netcfg,debian-installer/netcfg-static",
                         expect=("netcfg", ["debian-installer/netcfg",
                                            "debian-installer/netcfg-static"]))  # pylint: disable=line-too-long

    # single package
    _test_parse_cts_line(txt="bin/netcfg      debian-installer/netcfg-static",
                         expect=("bin/netcfg", ["debian-installer/netcfg-static"]))

    # package without path
    _test_parse_cts_line(txt="bin/netcfg        dnetcfg-static",
                         expect=("bin/netcfg", ["dnetcfg-static"]))

    # just single space separating cols
    _test_parse_cts_line(txt="bin/netcfg dnetcfg-static",
                         expect=("bin/netcfg", ["dnetcfg-static"]))

    # "Clients should correctly handle file names containing white space characters"
    _test_parse_cts_line(txt="some/file with   spaces    a/package",
                         expect=("some/file with   spaces", ["a/package"]))

    # Expect to parse as invalid
    # --------------------------
    # " A filename relative to the root directory, __without leading .__"
    _test_parse_cts_line(txt=".starts_with_period   a/package",
                         expect=None)

    # free text with no spacing
    _test_parse_cts_line(txt="some_free_text_no_space",
                         expect=None)

    # free text with at ends
    _test_parse_cts_line(txt=" some_free_text_with_space  ",
                         expect=None)
