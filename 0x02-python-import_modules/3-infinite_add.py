#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    i = 1
    while (sys.argv[i]):
        sum = sum + int(sys.argv[i])
        i = i + 1
    print("{}".format(sum))
