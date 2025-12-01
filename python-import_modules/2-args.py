#!/usr/bin/python3
import sys

if __name__ == "__main__":
    length = len(sys.argv) - 1

    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, sys.argv[i]))
