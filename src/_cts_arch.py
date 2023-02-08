""" see CtsArch below """

from itertools import islice
import operator
import pandas as pd

from ._man_parser import ManParser


# pylint: disable-next=too-few-public-methods
class CtsArch:
    """
        Encapsulates relevant information (data) from a content (index) file,
        and provides methods to query and display it
    """

    data: dict[str, int] = {}

    # ---------------------------------------------
    def __init__(self, data):
        self.data = data

    # ---------------------------------------------
    @classmethod
    def _from_file(cls, file_path) -> "CtsArch":
        """ create an instance from file at specified path  """
        inst = cls(ManParser.parse_cts_file(file_path=file_path))
        return inst

    # ---------------------------------------------
    @classmethod
    def _top_pkgs_from_file(cls, file_path, max_pkgs=None) -> list[tuple[str, int]]:
        """ return list of tuples: (package name, num of files in package):
        sorted by the latter, in descending order,
        calculated from contents (index) at file_path.
        If 'max_pkgs' is specified, the result is truncated to 'max_pkgs' before being returned.
        """

        inst = cls._from_file(file_path)

        # python 3.7+ has well-defined sort order for dict items
        sorted_tuples = sorted(inst.data.items(), key=operator.itemgetter(1), reverse=True)
        if not max_pkgs:
            return sorted_tuples
        return list(islice(sorted_tuples, max_pkgs))

    # ---------------------------------------------
    @classmethod
    def top_pkgs_str(cls, file_path, max_pkgs=None) -> str:
        """ str with tabular representation of result from _top_pkgs_from_file()
        """

        data = cls._top_pkgs_from_file(file_path, max_pkgs)
        dframe = pd.DataFrame(data, columns=['Package', 'Num Files'])

        # start index (zero based by default) at 1, for display to user
        dframe.index += 1
        ret = dframe.to_markdown()
        return ret
