#!/usr/bin/python3
if (len(argv) > 0):
    if (len(argv > 1)):
        print("{} arguments:".format(len(argv)))
        for i in argv:
            j = 1
            print("{}: {}".format(j, i))
            j = j + 1
    elif (len(argv) == 1):
        print("{} argument:")
        print("1: {}".format(argv[0]))
elif (len(argv) == 0):
    print("0 arguments.")
