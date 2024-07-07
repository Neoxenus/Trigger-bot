# utils.py
import sys

class Utils:
    
    def exiting():
        try:
            sys.exit()
        except:
            raise SystemExit
