""" Entry point for the application """

import sys
from ._man_app import ManApp

def async_test():
    import asyncio
    import time

    async def say_after(delay, what):
        await asyncio.sleep(delay)
        print(what)

    async def main():
        print(f"started at {time.strftime('%X')}")

        #await say_after(2, 'world')
        #await say_after(1, 'hello')

        await asyncio.gather(say_after(4, 'world'), say_after(1, 'hello'))


        print(f"finished at {time.strftime('%X')}")

    asyncio.run(main())

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
def test():
    class A:
        pass


    a = A();
    b1 = bool(a)

    a = None
    b2 = bool(a)
    halt =1

# ---------------------------------------
if __name__ == "__main__":
   # test()
   main()
   # async_test()
