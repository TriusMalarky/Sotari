from realityhandling.debugtests import *
from graphichandling.screen import *
from realityhandling.saves import *

if __name__ == "__main__":
    debug = True
    if debug:
        debugtest()

    save = Load()
    for i in save.log:
        print(i)
    Dump(save)
    app = Application()