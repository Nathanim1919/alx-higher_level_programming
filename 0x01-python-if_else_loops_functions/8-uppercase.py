#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if (ord(x) <= ord('Z') and ord(x) >= ord('A')):
            print("{}".format(x), end='')
        else:
            if (ord(x) >= ord('a') and ord(x) <= ord('z')):
                    print("{}".format(chr(ord(x) + 32)), end='')
