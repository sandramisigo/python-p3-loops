#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    return [x**2 for x in int_list]
    

def fizzbuzz():
    for i in range(1, 101):  # Loop through numbers from 1 to 100
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")  # Multiple of both 3 and 5
        elif i % 3 == 0:
            print("Fizz")  # Multiple of 3
        elif i % 5 == 0:
            print("Buzz")  # Multiple of 5
        else:
            print(i)  # Not a multiple of 3 or 5, print the number
