""" see ManLog below """

import logging
from typing import Optional


class ManLog:
    """ Logging functionality provided for rest of app - global (cross-cutting concern).
        Can be centrally configured here e.g.
            details of log file (and whether recycled)  or screen, custom formatting of messages etc
    Usage:
        ManLog().warn("my message", "some optional context")

    Singleton instance
            see eg https://python-patterns.guide/gang-of-four/singleton/
    """

    _instance: Optional["ManLog"] = None

    # ---------------------------------------------
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ManLog, cls).__new__(cls)
        return cls._instance

    # ---------------------------------------------
    def __init__(self):
        self.logger = logging.getLogger()
        # logging.basicConfig()

    # ---------------------------------------------
    @classmethod
    def warn(cls, mesg: str, context: str = "") -> None:
        """ log a warning to a centrally configured log sink """

        # mypy flags:  'error: Item "None" of "Optional[ManLog]" has no attribute "logger"'
        # if we don't ignore. see also https://github.com/python/mypy/issues/4805

        # pylint: disable-next=line-too-long   # pylint includes (inline mypy) comment in line length!
        cls._instance.logger.warning(f"Log(Ex_Core): {context} - {mesg}")  # type: ignore[union-attr]
