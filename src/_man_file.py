""" see ManFile below """

import os


class ManFile:
    """ Provides file and directory (path) services and lookup."""

    # ---------------------------------------------------------
    @classmethod
    def dir_path_root(cls) -> str:
        """ root dir (abs) path of project - contains 'src', 'test', 'prj' ... """
        dir_path_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return dir_path_parent

    # ---------------------------------------------------------
    @classmethod
    def dir_path_fixture(cls) -> str:
        """ abs dir path to test fixture dir """
        return cls.full_path(rel_path="test/fixture", root_path=cls.dir_path_root())

    # ---------------------------------------------------------
    @classmethod
    def dir_path_cache(cls) -> str:
        """ abs dir path to 'cache' dir """
        return cls.full_path(rel_path="tmp/cache", root_path=cls.dir_path_root())

    # ---------------------------------------------------------
    @classmethod
    def file_path_fixture(cls, file_name: str) -> str:
        """ full path of 'file_name' in fixture dir  """
        return cls.full_path(root_path=cls.dir_path_fixture(), rel_path=file_name)

    # ---------------------------------------------------------
    @classmethod
    def file_path_cache(cls, file_name: str) -> str:
        """ full path of 'file_name' in cache dir  """
        return cls.full_path(root_path=cls.dir_path_cache(), rel_path=file_name)

    # ---------------------------------------------------------
    @classmethod
    def full_path(cls, rel_path: str, root_path: str = None):
        """ full path of 'rel_path' within 'root_path """

        if root_path is None:
            root_path = cls.dir_path_root()

        ret = os.path.join(root_path, rel_path)
        return ret

    # ---------------------------------------------------------
    @classmethod
    def path_ensure_remove(cls, path: str):
        """ removes dir/file with 'path', if it exists.
        -Here be dragons-!
        Intercepting Filter Pattern:
        Using a centralized method like this for such dangerous operations helps mitigate
        danger such as this - localizes dangerous calls which might otherwise be scattered
        throughout the app. Allows us to do app-wide safety 'filtering/checking'
         eg. could verify here if path is in 'allowed' location such as 'tmpdir' or below project
         root, before complying
        """

        if os.path.exists(path):
            os.remove(path)

    # ---------------------------------------------------------
    @classmethod
    def path_ensure_exists(cls, path: str):
        """ ensure that dir/file with 'path' exists, creating (parents recursively) if necessary """
        print(f"start ... os.makedirs....{path}")
        os.makedirs(path, exist_ok=True)
        print(f"finish ... os.makedirs....{path}")

    # ---------------------------------------------------------
    @classmethod
    def path_exists(cls, path: str) -> bool:
        """ does dir/file with 'path' exist? """
        return os.path.exists(path)

# ---------------------------------------------------------
