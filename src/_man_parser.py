""" see ManParser below """

from typing import Optional
from bs4 import BeautifulSoup

from ._man_log import ManLog
from ._man_web import ManWeb


# -------------------------------------------
class ManParser:
    """ Parser for 'Listing' and 'Content' files  - see readme for terminology/nomenclature """

    @classmethod
    def parse_listing(cls, txt) -> dict[str, str]:
        """
        Parses the contents of a Listing File to a dict {name, url}
        eg.
      {
        "Contents-i386.gz" : "http://ftp.uk.debian.org/debian/dists/stable/main/Contents-i386.gz",
        ....
      }
        """

        soup = BeautifulSoup(txt, 'html.parser')
        anchors = soup.find_all("a")

        name_to_url: dict[str, str] = {}
        for anchor in anchors:
            href = anchor.get('href')
            href = ManWeb.ensure_absolute(href=href)
            txt = anchor.get_text().strip()
            txt_lower = txt.lower()

            if txt_lower.startswith("contents-") and txt_lower.endswith(".gz"):
                name_to_url[txt] = href

        return name_to_url

    # ---------------------------------------
    @classmethod
    def parse_listing_from_file(cls, file_path: str) -> dict[str, str]:
        """ Parses the Listing File at file path """

        with open(file_path, encoding='utf-8') as file:
            return cls.parse_listing(file.read())

    # ---------------------------------------
    @classmethod
    def parse_cts_file(cls, file_path: str) -> Optional[dict[str, int]]:
        """ Parses the contents (index) file at file path """

        pkg_to_cnt: dict[str, int] = {}
        with open(file_path, encoding='utf-8') as file:
            for idx, line in enumerate(file):
                cts_entry = cls.parse_cts_line(line)
                if not cts_entry:
                    ManLog().warn(f"ignoring line number: {idx} of Cts file: {file_path}"
                                  f" with contents: {line}")
                    continue
                pkgs = cts_entry[1]
                for pkg in pkgs:
                    # pkg not yet in dict
                    # - see Slatkin "Effective Python 2ed - Item 16: "Prefer get()...."
                    if (cnt := pkg_to_cnt.get(pkg)) is None:
                        cnt = 0
                    cnt += 1
                    pkg_to_cnt[pkg] = cnt
        return pkg_to_cnt

    # ---------------------------------------
    @classmethod
    def parse_cts_line(cls, txt_in: str) -> Optional[tuple[str, list[str]]]:
        """
        Parses a single line of a contents (index) file

        # from
        # https://wiki.debian.org/DebianRepository/Format?action=show&redirect=RepositoryFormat#A.22Contents.22_indices

            A filename relative to the root directory, without leading .
            A list of qualified package names, separated by comma.

            Clients should ignore lines not conforming to this scheme.
            Clients should correctly handle file names containing white space
            characters (possibly taking advantage of the fact that package names cannot include
             white space characters).
        """

        # split on last occurrence of whitespace
        parts = txt_in.rsplit(maxsplit=1)

        # invalid - see above
        if not len(parts) == 2:
            return None

        # remove any trailing whitespace from file
        file = parts[0].strip()

        packages_str = parts[1]

        # resolve multiple packages
        packages = packages_str.split(",")

        # invalid - see above
        if file.startswith("."):
            return None

        return file, packages
