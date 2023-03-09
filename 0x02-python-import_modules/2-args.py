#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) > 0):
        if (len(sys.argv) > 1):
            print("{} arguments:".format(len(sys.argv)))
            j = 0
            for i in sys.argv:
                if (j != 0):
                    print("{}: {}".format(j, i))
                j = j + 1
        elif (len(sys.argv) == 1):
            print("{} argument:")
            print("1: {}".format(sys.argv[1]))
    elif (len(sys.argv) == 0):
        print("0 arguments.")
