#! /bin/python3

import sys
from core.app import *
from core.isconnected import IsConnected

if __name__ == '__main__':

    if sys.argv[1].lower() == 'app':
        App().run_app()

    elif sys.argv[1].lower() == 'text':
        if IsConnected(ip=sys.argv[2]).isconnected():
            print(f'{sys.argv[2]} is is connected !')

    else:
        print('./main.py app or ./main.py text 127.0.0.1')

    

        


