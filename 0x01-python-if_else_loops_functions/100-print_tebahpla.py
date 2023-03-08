#!/usr/bin/python3
j = 1
i = 122
while i >= 97:
    if (j % 2 == 0):
        print("{}".format(chr(i - 32)), end="")
    else:
        print("{}".format(chr(i)), end="")
    i--
    j++
