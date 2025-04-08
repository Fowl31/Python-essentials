#!/usr/bin/env python3
from math_function import *

while True:
    choice = input("What operation would you like to carry out (quit): ")
    choice.lower()
    if choice == "quit":
        print("Quiting...")
        break
    elif choice == "rectangle":
        area_of_rect()
    elif choice == "circle":
        area_of_circle()
    elif choice == "factorial":
        fact()
    elif choice == "combination":
        combination()
    else:
        invalid()

        print("Invalid choice")
