#!/usr/bin/python3
def fizzbuzz():
    for i in range(101):
        if (i == 100):
            print("Buzz ")
        else:
            if (i > 0 and i % 3 == 0 and i % 5 == 0):
                print("FizzBuzz", end=", ")
            elif (i > 0 and i % 3 == 0):
                print("Fizz", end=" ")
            elif (i > 0 and i % 5 == 0):
                print("Buzz", end=" ")
            elif (i > 0):
                print(i, end=" ")
