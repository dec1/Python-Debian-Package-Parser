""" see ManWeb below """

import shutil
import os
from urllib.parse import urljoin
import requests

from tqdm.auto import tqdm
from ._man_file import ManFile


class ManWeb:
    """ Provides web services such as download of files, url path resolution """

    # ---------------------------------------------------------
    @classmethod
    def urlbase(cls) -> str:
        """ the base url used in this application. Any relative urls are considered
             relative to this
        """

        return "http://ftp.uk.debian.org/debian/dists/stable/main/"

    # ---------------------------------------------------------
    @classmethod
    def ensure_absolute(cls, href: str, base_url=None) -> str:
        """ href as an absolute url 'below' base_url """

        if not base_url:
            base_url = cls.urlbase()
        ret = urljoin(base_url, href)
        return ret

    # ---------------------------------------------------------
    @classmethod
    def full_path(cls, rel_path: str, base_path: str = None) -> str:
        """ the full path of rel_path relative to urlbase() """

        if base_path is None:
            base_path = cls.urlbase()

        rel_path = rel_path.strip().removeprefix("/")
        base_path = base_path.strip()
        if not base_path.endswith("/"):
            base_path += "/"
        ret = urljoin(base_path, rel_path)
        return ret

    # ---------------------------------------------------------
    @classmethod
    def download(cls, url: str, dir_path: str, want_lazy_download=None) -> str:
        """ download from url to local dir_path """

        if url.endswith('/'):
            # Assume we want to save it as index.html in the specified directory
            file_name = "index.html"
        else:
            # Otherwise, use the basename of the URL as the filename
            file_name = os.path.basename(url)

        # save the output to this file
        file_path = os.path.join(dir_path, file_name)

        # eg  for url: http://ftp.uk.debian.org/debian/dists/stable/main/
        # save url pointing to director as "index.html" file
        is_dir = os.path.isdir(file_path)
        print(f"is_dir = {is_dir}")
        if is_dir:
            file_path = os.path.join(file_path, "index.html")

        # could implement more complex caching strategy
        if want_lazy_download or cls._want_lazy_download():
            if ManFile.path_exists(file_path):
                print(f"already downloaded {url} ... reusing cached copy at {file_path}")
                return file_path

        print(f"downloading {url} ... to {dir_path}")
        print(f"dir_path:  {dir_path}")
        print(f"file_path:  {file_path}")
        # ensure local destination dir exists
        ManFile.path_ensure_exists(dir_path)

        # make an HTTP request within a context manager
        with requests.get(url, stream=True, timeout=5) as resp:
            # check header to get content length, in bytes

            ct_len_str = resp.headers.get("Content-Length")
            total_length = int(ct_len_str) if ct_len_str is not None else 0
            resp.raw.decode_content = True

            # show progress bar
            with tqdm.wrapattr(resp.raw, "read", total=total_length, desc="", colour="green") as raw:  # pylint: disable=line-too-long
                with open(file_path, 'wb') as output:
                    shutil.copyfileobj(raw, output)

        print(".... download complete")
        return file_path

    # ---------------------------------------------
    @classmethod
    def _want_lazy_download(cls) -> bool:
        """ Only actually download a file, the first time its requested.
        Thereafter, reuse the previously downloaded copy.
        Saves bandwidth, and speeds up execution. Is, however, more susceptible to
        failure - more difficult to recover from single corrupt download.
        Would need to know hash of remote files or have some other reliable method
        of verifying a downloaded file is valid.
        """
        # For now, prefer reliability to efficiency. Can remedy later, if efficiency becomes
        # (measurably) an issue
        return False
