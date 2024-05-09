""" Entry point for the application """

import sys
from ._man_app import ManApp

# ---------------------------------------
def main():
    """ delegates most work to the application manager, ManApp,
       to which it passes any command line arguments
    """

    args = sys.argv[1:]

    txt = ManApp.arch_stats_str(params=args)
    args_str = " ".join(args)
    if txt:
        print("")
        print(f"Package statistics for '{args_str}':")
        print(txt)
        print("")

# ---------------------------------------
if __name__ == "__main__":
   main()
