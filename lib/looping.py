#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    i = 10
    while i > 0:
        print(i)
        i -= 1
        
    print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    pass
    squared_integers = [int * int for int in int_list]
    return squared_integers

square_integers([1, 2, 3, 4, 5])

def fizzbuzz():
    # code goes here!
    pass
    i = 1
    for i in range(100):
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    
fizzbuzz()
