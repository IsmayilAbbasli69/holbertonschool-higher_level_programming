#!/usr/bin/python3
def uppercase(str):
    for c in str:
        # if c is lowercase (ASCII 97–122)
        if ord(c) >= 97 and ord(c) <= 122:
            # convert to uppercase (subtract 32)
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
