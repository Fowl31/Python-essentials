#!/usr/bin/env python3
import math

def area_of_circle():
    PI = math.pi
    inp = float(input("Enter radius: "))
    area = PI * (inp)**2

    print(f"The area of circle with radius {inp} is {area: .2f}")

def area_of_rect():
    width = float(input("Enter width: "))
    length = float(input("Enter length: "))
    area = width * length
    print(f"Area of rectangle is {area: .2f}")

def fact():
    try:
        inp = int(input("Enter num (must be > 1): "))
        if inp < 0:
            raise Exception("Must be an integer")
    except ValueError:
        print("Invalid data type")

    factorial = 1
    for i in range(1, inp+1):
        factorial = factorial * i

    print(f"Factorial of {inp} is {factorial}") 

def combination():
    while True:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2 (must be <= than num1): "))
        if num2 > num1:
            print("First number must be greater")
            continue
        break

    diff  = num1 - num2
    fact1 = 1
    for i in range(1, num1+1):
        fact1 = fact1 * i
        
    fact2 = 1
    for i in range(1, num2+1):
        fact2 = fact2 * i
    fact3 = 1
    for i in range(1, diff+1):
        fact3 = fact3 * i

    step1 = fact3*fact2
    step2 = fact1/step1
    print(f"The combination of {num1}C{num2} is {step2}")

lst = ["Quit","Circle", "Rectangle", "Factorial", "Combination"]
def invalid():
    for i, item in enumerate(lst):
        print(f"Index {i} \t {item}")



