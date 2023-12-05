#!/usr/bin/python3


"""
Module Name: 6-peak.py
Description: Provide a `find_peak` function
"""


def find_peak(list_of_integers):
    """Find the largest number in a list of unsorted integers
    """
    if (list_of_integers):
        peak = 0
        last = len(list_of_integers) - 1

        while (peak < last):
            mid = (peak + last) // 2

            if (list_of_integers[mid] < list_of_integers[mid + 1]):
                peak = mid + 1
            else:
                last = mid
        return list_of_integers[peak]
