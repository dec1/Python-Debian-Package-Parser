""" see ManApp below """

import argparse

from ._man_web import ManWeb
from ._man_file import ManFile
from ._man_log import ManLog
from ._man_parser import ManParser
from ._man_util import ManUtil
from ._cts_arch import CtsArch


# pylint: disable-next=too-few-public-methods
class ManApp:
    """
        Top level application "Manager".
        High (user) level application logic handled here.
        Delegates (delegation pattern) most work to second level 'managers' which it coordinates.
    """

    # ---------------------------------------------
    @classmethod
    def _arch_name_from_parms(cls, parms: list[str]) -> str:
        """ return architecture name from string list (command line parameters) """

        parser = argparse.ArgumentParser(
            prog='python -m src.main',
            description='displays statistics about the contents index for the '
                        'architecture you specify',
            epilog="example usage: > python -m src.main i386"
        )

        parser.add_argument('arch_name')
        args = parser.parse_args(parms)

        return args.arch_name

    # ---------------------------------------------
    @classmethod
    def _arch_file_name(cls, arch_name: str) -> str:
        """ calculates file name for a given architecture name
        eg returns 'Contents-i386.gz' when passed 'i386'
        """
        return f"Contents-{arch_name}.gz"

    # ---------------------------------------------
    @classmethod
    def _arch(cls, arch_file_name: str) -> str:
        """ calculates architecture name for a given  file name
        eg returns 'i386' when passed 'Contents-i386.gz'
        """
        return arch_file_name.removeprefix("Contents-").removesuffix(".gz")

    # ---------------------------------------------

    @classmethod
    def _url_for_cts_file(cls, file_name: str) -> str | None:
        """
            returns url where contents index file_name, can be downloaded
            eg. when passed:
                "Contents-i386.gz"
            should return:
                "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-i386.gz"

            The mapping is from the 'index.html' which is retrieved and parsed as necessary,
            to calculate the desired result
        """

        url_listing = ManWeb.full_path("")
        file_path = ManWeb.download(url=url_listing, dir_path=ManFile.dir_path_cache())
        name_to_url = ManParser.parse_listing_from_file(file_path)
        if (url := name_to_url.get(file_name)) is None:
            print(f"Sorry .... couldn't find \n  '{file_name}' at \n  '{url_listing}' ")
            print("Please pass one of......")
            keys = ("    " + cls._arch(file) for file in name_to_url)
            print(*keys, sep="\n")
            return None

        return url

    # ---------------------------------------------
    @classmethod
    def arch_stats_str(cls, params: list[str]) -> str | None:
        """
            raison d'etre: main public (api) service
            return a string representation of the statistics of the package encoded in
            the 'command line parameters' list, params
        """
        arch_name = cls._arch_name_from_parms(params)
        file_name = cls._arch_file_name(arch_name)
        print(f"collating for '{file_name}' .... ")

        url = cls._url_for_cts_file(file_name)
        if not url:
            print(f"couldn't resolve contents (index) file url for architecture '{arch_name}'")
            return None

        file_path = ManWeb.download(url=url, dir_path=ManFile.dir_path_cache())
        if not file_path:
            ManLog().warn(f"couldn't download contents (index) file '{file_name}'")
            return None

        print("extracting...")
        file_path_extracted = file_path.removesuffix(".gz") + "_extracted"
        ManUtil.unzip(file_path, file_path_extracted)
        ret = CtsArch.top_pkgs_str(file_path=file_path_extracted, max_pkgs=10)
        return ret
