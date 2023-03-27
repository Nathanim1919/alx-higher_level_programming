#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        n = 1
        for i in my_list:
            if (n <= x):
                print(i,end="")
            n+=1
        return n
        print()
    except:
        print("out of index")
