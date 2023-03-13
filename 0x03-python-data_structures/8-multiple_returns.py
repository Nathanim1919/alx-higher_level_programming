#!/usr/bin/python3
def multiple_returns(sentence):
    new_list = list(sentence)
    if len(new_list) > 0:
        return (len(new_list), new_list[0])
    else:
        return (0,None)
