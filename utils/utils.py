# utils.py
import sys

def exiting():
    try:
        sys.exit()
    except:
        raise SystemExit
