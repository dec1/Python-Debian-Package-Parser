""" see ManUtil below """

import hashlib
import shutil
import gzip


class ManUtil:
    """ Provides various utility functions eg for unzipping and calculating md5 hashes """

    # ---------------------------------------------------------
    @classmethod
    def unzip(cls, file_path_src: str, file_path_dst: str):
        """ unzip archive file_path_src to file_path_dst """

        with gzip.open(file_path_src, "rb") as f_in, open(file_path_dst, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

    # ---------------------------------------------------------
    @classmethod
    def md5_hash(cls, file_path: str):
        """ calculate the md5 hash for file_path"""

        with open(file_path, "rb") as file:
            return hashlib.md5(file.read()).hexdigest()
# ---------------------------------------------------------
