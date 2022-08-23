import os, sys
from core.app import *
from core.isconnected import IsConnected

if __name__ == '__main__':
    if sys.argv[1] == 'app':
        App().run_app()


    if sys.argv[1] == 'text':
        if IsConnected(ip=sys.argv[2]).isconnected():
            print(f'{sys.argv[2]} is is connected !')

        


